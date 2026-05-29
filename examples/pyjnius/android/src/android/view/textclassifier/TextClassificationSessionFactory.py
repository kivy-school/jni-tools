from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["TextClassificationSessionFactory"]

class TextClassificationSessionFactory(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/textclassifier/TextClassificationSessionFactory"
    createTextClassificationSession = JavaMethod("(Landroid/view/textclassifier/TextClassificationContext;)Landroid/view/textclassifier/TextClassifier;")