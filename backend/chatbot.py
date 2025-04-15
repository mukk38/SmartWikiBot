from transformers import pipeline
import wikipediaapi
from urllib.parse import unquote

class Chatbot:
    def __init__(self, domain):
        self.domain = domain
        self.history = []
        self.nlp = pipeline("question-answering", model="deepset/roberta-base-squad2")
        self.wiki = wikipediaapi.Wikipedia(
            language="en",
            user_agent="QA-Chatbot/1.0 (https://example.com; contact@example.com)"
        )

    def get_wiki_context(self, question):
        # Simple keyword extraction (split question into words)
        keywords = question.split()
        context = ""
        for keyword in keywords:
            # Decode URL-encoded keywords if necessary
            keyword = unquote(keyword)
            page = self.wiki.page(keyword)
            if page.exists():
                context = page.summary[:2000]  # Limit to avoid token overflow
                break
        if not context:
            # Try domain-specific category search as fallback
            category = f"Category:{self.domain.capitalize()}"
            cat = self.wiki.page(category)
            if cat.exists():
                for title in cat.categorymembers:
                    page = self.wiki.page(title)
                    if page.exists():
                        context = page.summary[:2000]
                        break
        return context if context else "No relevant Wikipedia page found."

    def get_response(self, question):
        # Fetch context from Wikipedia
        context = self.get_wiki_context(question)
        if context == "No relevant Wikipedia page found.":
            response = "Sorry, I couldn't find relevant information for your question."
        else:
            try:
                result = self.nlp(question=question, context=context)
                response = result["answer"]
            except Exception as e:
                response = f"Error processing question: {str(e)}"
        
        self.history.append({"question": question, "response": response})
        return response

    def get_history(self):
        return self.history