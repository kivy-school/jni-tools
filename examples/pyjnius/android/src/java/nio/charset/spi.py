from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class CharsetProvider(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/charset/spi/CharsetProvider"
    charsetForName = JavaMethod("(Ljava/lang/String;)Ljava/nio/charset/Charset;")
    charsets = JavaMethod("()Ljava/util/Iterator;")