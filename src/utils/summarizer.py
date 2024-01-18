from sumy.nlp.tokenizers import Tokenizer
from sumy.parsers.plaintext import PlaintextParser
from sumy.summarizers.luhn import LuhnSummarizer
import logging

from utils.config_loader import ConfigLoader


def summarize_conversation(conversation_history: str, summary_ratio: float = None) -> str:
    summary_ratio = summary_ratio or float(ConfigLoader().get_summary_ratio())
    try:
        parser = PlaintextParser.from_string(
            conversation_history, Tokenizer("english"))
        summarizer = LuhnSummarizer()
        total_sentences = len(list(parser.document.sentences))

        sentence_count = max(1, int(total_sentences * summary_ratio))

        summary = summarizer(parser.document, sentence_count)
        summarized_text = ' '.join([str(sentence) for sentence in summary])
        return summarized_text
    except Exception as e:
        logging.error(f"Summarization error: {e}")
        return ""
