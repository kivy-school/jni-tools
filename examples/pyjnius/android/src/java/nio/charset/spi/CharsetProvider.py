from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CharsetProvider"]

class CharsetProvider(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/charset/spi/CharsetProvider"
    charsetForName = JavaMethod("(Ljava/lang/String;)Ljava/nio/charset/Charset;")
    charsets = JavaMethod("()Ljava/util/Iterator;")