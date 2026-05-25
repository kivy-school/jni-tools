from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Normalizer"]

class Normalizer(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/text/Normalizer"
    normalize = JavaStaticMethod("(Ljava/lang/CharSequence;Ljava/text/Normalizer$Form;)Ljava/lang/String;")
    isNormalized = JavaStaticMethod("(Ljava/lang/CharSequence;Ljava/text/Normalizer$Form;)Z")

    class Form(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "java/text/Normalizer/Form"
        values = JavaStaticMethod("()[Ljava/text/Normalizer$Form;")
        valueOf = JavaStaticMethod("(Ljava/lang/String;)Ljava/text/Normalizer$Form;")
        NFD = JavaStaticField("Ljava/text/Normalizer/Form;")
        NFC = JavaStaticField("Ljava/text/Normalizer/Form;")
        NFKD = JavaStaticField("Ljava/text/Normalizer/Form;")
        NFKC = JavaStaticField("Ljava/text/Normalizer/Form;")