from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DataInputStream"]

class DataInputStream(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/io/DataInputStream"
    __javaconstructor__ = [("(Ljava/io/InputStream;)V", False)]
    read = JavaMultipleMethod([("([B)I", False, False), ("([BII)I", False, False)])
    readFully = JavaMultipleMethod([("([B)V", False, False), ("([BII)V", False, False)])
    skipBytes = JavaMethod("(I)I")
    readBoolean = JavaMethod("()Z")
    readByte = JavaMethod("()B")
    readUnsignedByte = JavaMethod("()I")
    readShort = JavaMethod("()S")
    readUnsignedShort = JavaMethod("()I")
    readChar = JavaMethod("()C")
    readInt = JavaMethod("()I")
    readLong = JavaMethod("()J")
    readFloat = JavaMethod("()F")
    readDouble = JavaMethod("()D")
    readLine = JavaMethod("()Ljava/lang/String;")
    readUTF = JavaMultipleMethod([("()Ljava/lang/String;", False, False), ("(Ljava/io/DataInput;)Ljava/lang/String;", True, False)])