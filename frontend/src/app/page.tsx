'use client';
import SearchBox from '@/app/components/searchBox';
import SearchResults from '@/app/components/searchResults';
import UploadForm from '@/app/components/uploadForm';
import React, { useState } from 'react';

export default function Home() {
  const [results, setResults] = useState([]);

  return (
    <main className="max-w-3xl mx-auto p-8">
      <h1 className="text-2xl font-bold mb-4">My RAG App</h1>
      <UploadForm />
      <SearchBox onResults={setResults} />
      <SearchResults results={results} />
    </main>
  );
}
