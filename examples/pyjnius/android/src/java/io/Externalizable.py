from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Externalizable"]

class Externalizable(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/io/Externalizable"
    writeExternal = JavaMethod("(Ljava/io/ObjectOutput;)V")
    readExternal = JavaMethod("(Ljava/io/ObjectInput;)V")