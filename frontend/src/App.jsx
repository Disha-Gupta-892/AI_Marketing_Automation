import React, { useState } from 'react';
import { Upload, Wand2, ImageIcon, Share2, CheckCircle, Loader2, RefreshCw } from 'lucide-react';

const App = () => {
  const [step, setStep] = useState(1);
  const [loading, setLoading] = useState(false);
  const [productData, setProductData] = useState({
    name: '',
    features: ['', '', ''],
    tone: 'premium',
    image: null,
    imagePreview: null
  });
  const [generatedContent, setGeneratedContent] = useState(null);
  const [selectedOptions, setSelectedOptions] = useState({
    headline: 0,
    linkedin: 0,
    instagram: 0,
    facebook: 0
  });
  const [resizedCreatives, setResizedCreatives] = useState(null);
  const [publishStatus, setPublishStatus] = useState(null);

  const API_BASE = 'http://localhost:8000';

  const handleImageUpload = (e) => {
    const file = e.target.files[0];
    if (file) {
      setProductData({
        ...productData,
        image: file,
        imagePreview: URL.createObjectURL(file)
      });
    }
  };

  const handleFeatureChange = (index, value) => {
    const newFeatures = [...productData.features];
    newFeatures[index] = value;
    setProductData({ ...productData, features: newFeatures });
  };

  const addFeature = () => {
    if (productData.features.length < 5) {
      setProductData({
        ...productData,
        features: [...productData.features, '']
      });
    }
  };

  const generateCopy = async () => {
    setLoading(true);
    try {
      const formData = new FormData();
      formData.append('image', productData.image);
      formData.append('product_name', productData.name);
      formData.append('features', JSON.stringify(productData.features.filter(f => f)));
      formData.append('tone', productData.tone);

      const response = await fetch(`${API_BASE}/api/generate-copy`, {
        method: 'POST',
        body: formData
      });

      const data = await response.json();
      setGeneratedContent(data);
      setStep(2);
    } catch (error) {
      console.error('Error generating copy:', error);
      alert('Failed to generate copy. Please try again.');
    } finally {
      setLoading(false);
    }
  };

  const regenerateCopy = async () => {
    await generateCopy();
  };

  const approveAndResize = async () => {
    setLoading(true);
    try {
      const response = await fetch(`${API_BASE}/api/create-creatives`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          campaign_id: generatedContent.campaign_id,
          selected_headline: selectedOptions.headline,
          selected_captions: {
            linkedin: selectedOptions.linkedin,
            instagram: selectedOptions.instagram,
            facebook: selectedOptions.facebook
          }
        })
      });

      const data = await response.json();
      setResizedCreatives(data);
      setStep(3);
    } catch (error) {
      console.error('Error creating creatives:', error);
      alert('Failed to create creatives. Please try again.');
    } finally {
      setLoading(false);
    }
  };

  const publishToSocial = async () => {
    setLoading(true);
    try {
      const response = await fetch(`${API_BASE}/api/publish`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          campaign_id: generatedContent.campaign_id
        })
      });

      const data = await response.json();
      setPublishStatus(data);
      setStep(4);
    } catch (error) {
      console.error('Error publishing:', error);
      alert('Failed to publish. Please try again.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-50 to-indigo-100 p-6">
      <div className="max-w-6xl mx-auto">
        {/* Header */}
        <div className="text-center mb-8">
          <h1 className="text-4xl font-bold text-gray-800 mb-2">
            AI-First Marketing Automation
          </h1>
          <p className="text-gray-600">Generate, Review, and Publish Marketing Creatives</p>
        </div>

        {/* Progress Steps */}
        <div className="bg-white rounded-lg shadow-md p-6 mb-6">
          <div className="flex items-center justify-between">
            {[
              { num: 1, label: 'Upload & Input', icon: Upload },
              { num: 2, label: 'Review & Approve', icon: CheckCircle },
              { num: 3, label: 'Preview Creatives', icon: ImageIcon },
              { num: 4, label: 'Publish', icon: Share2 }
            ].map(({ num, label, icon: Icon }) => (
              <div key={num} className="flex items-center">
                <div className={`flex items-center justify-center w-12 h-12 rounded-full ${
                  step >= num ? 'bg-indigo-600 text-white' : 'bg-gray-200 text-gray-500'
                }`}>
                  {step > num ? <CheckCircle size={24} /> : <Icon size={24} />}
                </div>
                <span className={`ml-2 font-medium ${
                  step >= num ? 'text-indigo-600' : 'text-gray-400'
                }`}>{label}</span>
                {num < 4 && <div className="w-16 h-1 bg-gray-200 mx-4" />}
              </div>
            ))}
          </div>
        </div>

        {/* Step 1: Upload & Input */}
        {step === 1 && (
          <div className="bg-white rounded-lg shadow-md p-8">
            <h2 className="text-2xl font-bold text-gray-800 mb-6">Product Information</h2>
            
            {/* Image Upload */}
            <div className="mb-6">
              <label className="block text-sm font-medium text-gray-700 mb-2">
                Product Image
              </label>
              <div className="border-2 border-dashed border-gray-300 rounded-lg p-8 text-center hover:border-indigo-500 transition-colors">
                {productData.imagePreview ? (
                  <div className="relative">
                    <img src={productData.imagePreview} alt="Product" className="max-h-64 mx-auto rounded" />
                    <button
                      onClick={() => setProductData({ ...productData, image: null, imagePreview: null })}
                      className="absolute top-2 right-2 bg-red-500 text-white px-3 py-1 rounded text-sm"
                    >
                      Remove
                    </button>
                  </div>
                ) : (
                  <label className="cursor-pointer">
                    <Upload className="mx-auto mb-4 text-gray-400" size={48} />
                    <p className="text-gray-600">Click to upload product image</p>
                    <input
                      type="file"
                      accept="image/*"
                      onChange={handleImageUpload}
                      className="hidden"
                    />
                  </label>
                )}
              </div>
            </div>

            {/* Product Name */}
            <div className="mb-6">
              <label className="block text-sm font-medium text-gray-700 mb-2">
                Product Name
              </label>
              <input
                type="text"
                value={productData.name}
                onChange={(e) => setProductData({ ...productData, name: e.target.value })}
                placeholder="e.g., Premium Wireless Headphones"
                className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-indigo-500 focus:border-transparent"
              />
            </div>

            {/* Features */}
            <div className="mb-6">
              <label className="block text-sm font-medium text-gray-700 mb-2">
                Key Features (3-5)
              </label>
              {productData.features.map((feature, index) => (
                <input
                  key={index}
                  type="text"
                  value={feature}
                  onChange={(e) => handleFeatureChange(index, e.target.value)}
                  placeholder={`Feature ${index + 1}`}
                  className="w-full px-4 py-2 border border-gray-300 rounded-lg mb-2 focus:ring-2 focus:ring-indigo-500 focus:border-transparent"
                />
              ))}
              {productData.features.length < 5 && (
                <button
                  onClick={addFeature}
                  className="text-indigo-600 text-sm font-medium hover:text-indigo-700"
                >
                  + Add Feature
                </button>
              )}
            </div>

            {/* Tone */}
            <div className="mb-6">
              <label className="block text-sm font-medium text-gray-700 mb-2">
                Brand Tone
              </label>
              <select
                value={productData.tone}
                onChange={(e) => setProductData({ ...productData, tone: e.target.value })}
                className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-indigo-500 focus:border-transparent"
              >
                <option value="premium">Premium</option>
                <option value="playful">Playful</option>
                <option value="minimal">Minimal</option>
                <option value="luxury">Luxury</option>
                <option value="professional">Professional</option>
              </select>
            </div>

            <button
              onClick={generateCopy}
              disabled={!productData.image || !productData.name || loading}
              className="w-full bg-indigo-600 text-white py-3 rounded-lg font-medium hover:bg-indigo-700 disabled:bg-gray-300 disabled:cursor-not-allowed flex items-center justify-center"
            >
              {loading ? (
                <>
                  <Loader2 className="animate-spin mr-2" size={20} />
                  Generating with AI...
                </>
              ) : (
                <>
                  <Wand2 className="mr-2" size={20} />
                  Generate Marketing Copy
                </>
              )}
            </button>
          </div>
        )}

        {/* Step 2: Review & Approve */}
        {step === 2 && generatedContent && (
          <div className="bg-white rounded-lg shadow-md p-8">
            <div className="flex justify-between items-center mb-6">
              <h2 className="text-2xl font-bold text-gray-800">Review Generated Content</h2>
              <button
                onClick={regenerateCopy}
                disabled={loading}
                className="flex items-center px-4 py-2 bg-gray-100 text-gray-700 rounded-lg hover:bg-gray-200"
              >
                <RefreshCw className="mr-2" size={16} />
                Regenerate
              </button>
            </div>

            {/* Headlines */}
            <div className="mb-8">
              <h3 className="text-lg font-semibold text-gray-700 mb-4">Select Headline</h3>
              <div className="space-y-3">
                {generatedContent.headlines.map((headline, index) => (
                  <label
                    key={index}
                    className={`block p-4 border-2 rounded-lg cursor-pointer transition-all ${
                      selectedOptions.headline === index
                        ? 'border-indigo-600 bg-indigo-50'
                        : 'border-gray-200 hover:border-gray-300'
                    }`}
                  >
                    <input
                      type="radio"
                      name="headline"
                      checked={selectedOptions.headline === index}
                      onChange={() => setSelectedOptions({ ...selectedOptions, headline: index })}
                      className="mr-3"
                    />
                    <span className="font-medium">{headline}</span>
                  </label>
                ))}
              </div>
            </div>

            {/* Platform Captions */}
            {['linkedin', 'instagram', 'facebook'].map((platform) => (
              <div key={platform} className="mb-8">
                <h3 className="text-lg font-semibold text-gray-700 mb-4 capitalize">
                  {platform} Caption
                </h3>
                <div className="space-y-3">
                  {generatedContent.captions[platform].map((caption, index) => (
                    <label
                      key={index}
                      className={`block p-4 border-2 rounded-lg cursor-pointer transition-all ${
                        selectedOptions[platform] === index
                          ? 'border-indigo-600 bg-indigo-50'
                          : 'border-gray-200 hover:border-gray-300'
                      }`}
                    >
                      <input
                        type="radio"
                        name={platform}
                        checked={selectedOptions[platform] === index}
                        onChange={() => setSelectedOptions({ ...selectedOptions, [platform]: index })}
                        className="mr-3"
                      />
                      <span className="text-sm">{caption}</span>
                    </label>
                  ))}
                </div>
              </div>
            ))}

            <button
              onClick={approveAndResize}
              disabled={loading}
              className="w-full bg-indigo-600 text-white py-3 rounded-lg font-medium hover:bg-indigo-700 flex items-center justify-center"
            >
              {loading ? (
                <>
                  <Loader2 className="animate-spin mr-2" size={20} />
                  Creating Creatives...
                </>
              ) : (
                <>
                  <CheckCircle className="mr-2" size={20} />
                  Approve & Create Creatives
                </>
              )}
            </button>
          </div>
        )}

        {/* Step 3: Preview Creatives */}
        {step === 3 && resizedCreatives && (
          <div className="bg-white rounded-lg shadow-md p-8">
            <h2 className="text-2xl font-bold text-gray-800 mb-6">Platform-Specific Creatives</h2>
            
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 mb-8">
              {resizedCreatives.creatives.map((creative, index) => (
                <div key={index} className="border rounded-lg p-4">
                  <h3 className="font-semibold text-gray-700 mb-2">{creative.platform}</h3>
                  <p className="text-sm text-gray-500 mb-3">{creative.size}</p>
                  <img
                    src={`${API_BASE}${creative.image_url}`}
                    alt={creative.platform}
                    className="w-full rounded shadow-md"
                  />
                  <p className="text-xs text-gray-600 mt-3 line-clamp-3">{creative.caption}</p>
                </div>
              ))}
            </div>

            <button
              onClick={publishToSocial}
              disabled={loading}
              className="w-full bg-green-600 text-white py-3 rounded-lg font-medium hover:bg-green-700 flex items-center justify-center"
            >
              {loading ? (
                <>
                  <Loader2 className="animate-spin mr-2" size={20} />
                  Publishing...
                </>
              ) : (
                <>
                  <Share2 className="mr-2" size={20} />
                  Publish to Social Media
                </>
              )}
            </button>
          </div>
        )}

        {/* Step 4: Publish Success */}
        {step === 4 && publishStatus && (
          <div className="bg-white rounded-lg shadow-md p-8 text-center">
            <CheckCircle className="mx-auto text-green-500 mb-4" size={64} />
            <h2 className="text-2xl font-bold text-gray-800 mb-4">Successfully Published!</h2>
            
            <div className="space-y-4 max-w-2xl mx-auto">
              {publishStatus.results.map((result, index) => (
                <div key={index} className="bg-gray-50 p-4 rounded-lg">
                  <h3 className="font-semibold text-gray-700 capitalize">{result.platform}</h3>
                  <p className={`text-sm ${result.success ? 'text-green-600' : 'text-red-600'}`}>
                    {result.message}
                  </p>
                  {result.post_url && (
                    <a
                      href={result.post_url}
                      target="_blank"
                      rel="noopener noreferrer"
                      className="text-indigo-600 text-sm hover:underline"
                    >
                      View Post
                    </a>
                  )}
                </div>
              ))}
            </div>

            <button
              onClick={() => {
                setStep(1);
                setProductData({ name: '', features: ['', '', ''], tone: 'premium', image: null, imagePreview: null });
                setGeneratedContent(null);
                setSelectedOptions({ headline: 0, linkedin: 0, instagram: 0, facebook: 0 });
                setResizedCreatives(null);
                setPublishStatus(null);
              }}
              className="mt-6 px-6 py-3 bg-indigo-600 text-white rounded-lg font-medium hover:bg-indigo-700"
            >
              Create New Campaign
            </button>
          </div>
        )}
      </div>
    </div>
  );
};

export default App;