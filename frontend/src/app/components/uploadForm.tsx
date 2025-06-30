'use client';
// components/UploadForm.tsx
import React, { useState } from 'react';

export default function UploadForm() {
  const [file, setFile] = useState<File | null>(null);
  const [status, setStatus] = useState('');

  const handleUpload = async () => {
    if (!file) return;
    const formData = new FormData();
    formData.append('file', file);

    const res = await fetch('http://localhost:8000/upload', {
      method: 'POST',
      body: formData,
    });

    if (res.ok) {
      setStatus('Upload successful!');
    } else {
      setStatus('Upload failed.');
    }
  };

  return (
    <div className="p-4 border rounded">
      <input
        type="file"
        onChange={(e) => setFile(e.target.files?.[0] ?? null)}
      />
      <button onClick={handleUpload} className="bg-blue-500 text-white px-4 py-2 ml-2 rounded">
        Upload
      </button>
      <p>{status}</p>
    </div>
  );
}
