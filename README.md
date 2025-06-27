Learning project to help dive into AI; sample using RAG pipelines, vector DB and LLM api. Plus some React + Next.js for practice.

What this does:
This is a RAG(Retrieval-Augmented Generation) app

1) Lets you upload a number of pdf and word documents, with the upload api endpoint.
2) Then allows you search via a semantic query, to retrieve a document uploaded, that best matches.

For this project im utilising Open AI's developer api to create an embedding for my uploaded documents. An embedding is like a shape, or a puzzle piece that matches the text uploaded, in the form of an array of numbers (a vector). When the application recieves a document, we chop it up and send each chunk of text to OpenAI, and it returns a list of numbers that represent the text’s meaning — like a unique fingerprint or puzzle piece for each one.

We then store those embeddings/chunks in a vector (postgres) database.

A vector Database as opposed to a standard rdb, uses vector indexes rather than specific values like an id. Which allows a fast nearest-neighbor search. Each record stores embeddings in a special vector column. The database builds an index optimized for neighbor queries. I.e. Like a phonebook that rather than being sorted alphabetically, arranges similar-sounding names to be clustered together to allow finding the closest matches.

When a user searches we forward on their search term/query to the OpenAI llm once again to get its embedding / vector -  an query this vector against the existing ones in our database. Behind the scenes some fancy geometric math happens; fancy math like cosine similarity or Euclidean distance. And we return the top 3 results, based on their distance score. Simple really.