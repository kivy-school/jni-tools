from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["TextClassificationManager"]

class TextClassificationManager(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/textclassifier/TextClassificationManager"
    setTextClassificationSessionFactory = JavaMethod("(Landroid/view/textclassifier/TextClassificationSessionFactory;)V")
    getTextClassifier = JavaMethod("()Landroid/view/textclassifier/TextClassifier;")
    setTextClassifier = JavaMethod("(Landroid/view/textclassifier/TextClassifier;)V")
    createTextClassificationSession = JavaMethod("(Landroid/view/textclassifier/TextClassificationContext;)Landroid/view/textclassifier/TextClassifier;")