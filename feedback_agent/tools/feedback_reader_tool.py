from typing import List, TypedDict, Literal, Any

class Feedback(TypedDict):
    id: str
    text: str
    source: Literal["email", "chat", "survey"]

feedback_store: List[Feedback] = [
    {
        "id": "1",
        "text": "I love the product!",
        "source": "email"
    },
    {
        "id": "2",
        "text": "The product is great!",
        "source": "chat"
    },
    {
        "id": "3",
        "text": "I had a great experience with the product.",
        "source": "survey"
    },
    {
        "id": "4",
        "text": "I had a bad experience with the product.",
        "source": "survey"
    },
    {
        "id": "5",
        "text": "I had a great experience with the product.",
        "source": "survey"
    },
    {
        "id": "6",
        "text": "The mobile app crashes when I try to upload photos.",
        "source": "chat"
    },
    {
        "id": "7",
        "text": "Please add dark mode — my eyes would thank you.",
        "source": "email"
    },
    {
        "id": "8",
        "text": "Checkout took too long and timed out twice.",
        "source": "survey"
    },
    {
        "id": "9",
        "text": "Love the new onboarding flow — very intuitive.",
        "source": "email"
    },
    {
        "id": "10",
        "text": "I keep getting duplicate notifications for the same event.",
        "source": "chat"
    },
    {
        "id": "11",
        "text": "Feature request: allow exporting reports as CSV.",
        "source": "email"
    },
    {
        "id": "12",
        "text": "Support was helpful and resolved my issue quickly.",
        "source": "chat"
    },
    {
        "id": "13",
        "text": "The pricing page is confusing. Please clarify plan limits.",
        "source": "survey"
    },
    {
        "id": "14",
        "text": "I experienced a payment failure but was charged anyway.",
        "source": "email"
    },
    {
        "id": "15",
        "text": "Add more integrations with popular calendar apps.",
        "source": "survey"
    },
    {
        "id": "16",
        "text": "Translations are inaccurate in the French locale.",
        "source": "chat"
    },
    {
        "id": "17",
        "text": "The search results are missing recent items.",
        "source": "email"
    },
    {
        "id": "18",
        "text": "Great value for money — will recommend to colleagues.",
        "source": "survey"
    }
]

def query_feedback(**kwargs: Any) -> List[Feedback]:
    return feedback_store
