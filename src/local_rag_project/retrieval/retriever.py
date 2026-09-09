from local_rag_project.embeddings.embedder import Embedder
from local_rag_project.retrieval.similarity import cosine_similarity


class Retriever:
    def __init__(self, chunks: list[str]):
        self.chunks = chunks
        self.embedder = Embedder()

        print("Creating chunk embeddings...")

        self.embeddings = self.embedder.embed_texts(chunks)

    def search(
        self,
        query: str,
        top_k: int = 3,
    ) -> list[tuple[str, float]]:

        query_embedding = self.embedder.embed_text(query)

        results = []

        for chunk, embedding in zip(
            self.chunks,
            self.embeddings,
        ):
            score = cosine_similarity(
                query_embedding,
                embedding,
            )

            results.append((chunk, score))

        results.sort(
            key=lambda item: item[1],
            reverse=True,
        )

        return results[:top_k]