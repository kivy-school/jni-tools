from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ObjectInputStream"]

class ObjectInputStream(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/io/ObjectInputStream"
    __javaconstructor__ = [("(Ljava/io/InputStream;)V", False), ("()V", False)]
    readObject = JavaMethod("()Ljava/lang/Object;")
    readObjectOverride = JavaMethod("()Ljava/lang/Object;")
    readUnshared = JavaMethod("()Ljava/lang/Object;")
    defaultReadObject = JavaMethod("()V")
    readFields = JavaMethod("()Ljava/io/ObjectInputStream$GetField;")
    registerValidation = JavaMethod("(Ljava/io/ObjectInputValidation;I)V")
    resolveClass = JavaMethod("(Ljava/io/ObjectStreamClass;)Ljava/lang/Class;")
    resolveProxyClass = JavaMethod("([Ljava/lang/String;)Ljava/lang/Class;")
    resolveObject = JavaMethod("(Ljava/lang/Object;)Ljava/lang/Object;")
    enableResolveObject = JavaMethod("(Z)Z")
    readStreamHeader = JavaMethod("()V")
    readClassDescriptor = JavaMethod("()Ljava/io/ObjectStreamClass;")
    read = JavaMultipleMethod([("()I", False, False), ("([BII)I", False, False)])
    available = JavaMethod("()I")
    close = JavaMethod("()V")
    readBoolean = JavaMethod("()Z")
    readByte = JavaMethod("()B")
    readUnsignedByte = JavaMethod("()I")
    readChar = JavaMethod("()C")
    readShort = JavaMethod("()S")
    readUnsignedShort = JavaMethod("()I")
    readInt = JavaMethod("()I")
    readLong = JavaMethod("()J")
    readFloat = JavaMethod("()F")
    readDouble = JavaMethod("()D")
    readFully = JavaMultipleMethod([("([B)V", False, False), ("([BII)V", False, False)])
    skipBytes = JavaMethod("(I)I")
    readLine = JavaMethod("()Ljava/lang/String;")
    readUTF = JavaMethod("()Ljava/lang/String;")

    class GetField(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "java/io/ObjectInputStream/GetField"
        __javaconstructor__ = [("()V", False)]
        getObjectStreamClass = JavaMethod("()Ljava/io/ObjectStreamClass;")
        defaulted = JavaMethod("(Ljava/lang/String;)Z")
        get = JavaMultipleMethod([("(Ljava/lang/String;Z)Z", False, False), ("(Ljava/lang/String;B)B", False, False), ("(Ljava/lang/String;C)C", False, False), ("(Ljava/lang/String;S)S", False, False), ("(Ljava/lang/String;I)I", False, False), ("(Ljava/lang/String;J)J", False, False), ("(Ljava/lang/String;F)F", False, False), ("(Ljava/lang/String;D)D", False, False), ("(Ljava/lang/String;Ljava/lang/Object;)Ljava/lang/Object;", False, False)])