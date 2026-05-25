from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Externalizable"]

class Externalizable(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "java/io/Externalizable"
    writeExternal = JavaMethod("(Ljava/io/ObjectOutput;)V")
    readExternal = JavaMethod("(Ljava/io/ObjectInput;)V")