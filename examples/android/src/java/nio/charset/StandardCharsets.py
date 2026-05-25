from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["StandardCharsets"]

class StandardCharsets(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/charset/StandardCharsets"
    ISO_8859_1 = JavaStaticField("Ljava/nio/charset/Charset;")
    US_ASCII = JavaStaticField("Ljava/nio/charset/Charset;")
    UTF_16 = JavaStaticField("Ljava/nio/charset/Charset;")
    UTF_16BE = JavaStaticField("Ljava/nio/charset/Charset;")
    UTF_16LE = JavaStaticField("Ljava/nio/charset/Charset;")
    UTF_8 = JavaStaticField("Ljava/nio/charset/Charset;")