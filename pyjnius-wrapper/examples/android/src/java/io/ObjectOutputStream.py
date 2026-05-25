from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ObjectOutputStream"]

class ObjectOutputStream(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/io/ObjectOutputStream"
    __javaconstructor__ = [("(Ljava/io/OutputStream;)V", False), ("()V", False)]
    useProtocolVersion = JavaMethod("(I)V")
    writeObject = JavaMethod("(Ljava/lang/Object;)V")
    writeObjectOverride = JavaMethod("(Ljava/lang/Object;)V")
    writeUnshared = JavaMethod("(Ljava/lang/Object;)V")
    defaultWriteObject = JavaMethod("()V")
    putFields = JavaMethod("()Ljava/io/ObjectOutputStream$PutField;")
    writeFields = JavaMethod("()V")
    reset = JavaMethod("()V")
    annotateClass = JavaMethod("(Ljava/lang/Class;)V")
    annotateProxyClass = JavaMethod("(Ljava/lang/Class;)V")
    replaceObject = JavaMethod("(Ljava/lang/Object;)Ljava/lang/Object;")
    enableReplaceObject = JavaMethod("(Z)Z")
    writeStreamHeader = JavaMethod("()V")
    writeClassDescriptor = JavaMethod("(Ljava/io/ObjectStreamClass;)V")
    write = JavaMultipleMethod([("(I)V", False, False), ("([B)V", False, False), ("([BII)V", False, False)])
    flush = JavaMethod("()V")
    drain = JavaMethod("()V")
    close = JavaMethod("()V")
    writeBoolean = JavaMethod("(Z)V")
    writeByte = JavaMethod("(I)V")
    writeShort = JavaMethod("(I)V")
    writeChar = JavaMethod("(I)V")
    writeInt = JavaMethod("(I)V")
    writeLong = JavaMethod("(J)V")
    writeFloat = JavaMethod("(F)V")
    writeDouble = JavaMethod("(D)V")
    writeBytes = JavaMethod("(Ljava/lang/String;)V")
    writeChars = JavaMethod("(Ljava/lang/String;)V")
    writeUTF = JavaMethod("(Ljava/lang/String;)V")

    class PutField(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "java/io/ObjectOutputStream/PutField"
        __javaconstructor__ = [("()V", False)]
        put = JavaMultipleMethod([("(Ljava/lang/String;Z)V", False, False), ("(Ljava/lang/String;B)V", False, False), ("(Ljava/lang/String;C)V", False, False), ("(Ljava/lang/String;S)V", False, False), ("(Ljava/lang/String;I)V", False, False), ("(Ljava/lang/String;J)V", False, False), ("(Ljava/lang/String;F)V", False, False), ("(Ljava/lang/String;D)V", False, False), ("(Ljava/lang/String;Ljava/lang/Object;)V", False, False)])
        write = JavaMethod("(Ljava/io/ObjectOutput;)V")