from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["StandardCharsets"]

class StandardCharsets(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/charset/StandardCharsets"
    US_ASCII = JavaStaticField("Ljava/nio/charset/Charset;")
    ISO_8859_1 = JavaStaticField("Ljava/nio/charset/Charset;")
    UTF_8 = JavaStaticField("Ljava/nio/charset/Charset;")
    UTF_16BE = JavaStaticField("Ljava/nio/charset/Charset;")
    UTF_16LE = JavaStaticField("Ljava/nio/charset/Charset;")
    UTF_16 = JavaStaticField("Ljava/nio/charset/Charset;")
    UTF_32BE = JavaStaticField("Ljava/nio/charset/Charset;")
    UTF_32LE = JavaStaticField("Ljava/nio/charset/Charset;")
    UTF_32 = JavaStaticField("Ljava/nio/charset/Charset;")