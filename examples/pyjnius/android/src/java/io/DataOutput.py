from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DataOutput"]

class DataOutput(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/io/DataOutput"
    write = JavaMultipleMethod([("([BII)V", False, False), ("([B)V", False, False), ("(I)V", False, False)])
    writeInt = JavaMethod("(I)V")
    writeUTF = JavaMethod("(Ljava/lang/String;)V")
    writeBytes = JavaMethod("(Ljava/lang/String;)V")
    writeChar = JavaMethod("(I)V")
    writeFloat = JavaMethod("(F)V")
    writeLong = JavaMethod("(J)V")
    writeByte = JavaMethod("(I)V")
    writeShort = JavaMethod("(I)V")
    writeBoolean = JavaMethod("(Z)V")
    writeDouble = JavaMethod("(D)V")
    writeChars = JavaMethod("(Ljava/lang/String;)V")