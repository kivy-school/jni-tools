from typing import Any, ClassVar, overload
from android.view.textclassifier.TextClassificationContext import TextClassificationContext
from android.view.textclassifier.TextClassifier import TextClassifier

class TextClassificationSessionFactory:
    def createTextClassificationSession(self, arg0: TextClassificationContext) -> TextClassifier: ...
