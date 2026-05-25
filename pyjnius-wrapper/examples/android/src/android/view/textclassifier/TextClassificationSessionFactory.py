from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["TextClassificationSessionFactory"]

class TextClassificationSessionFactory(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/textclassifier/TextClassificationSessionFactory"
    createTextClassificationSession = JavaMethod("(Landroid/view/textclassifier/TextClassificationContext;)Landroid/view/textclassifier/TextClassifier;")