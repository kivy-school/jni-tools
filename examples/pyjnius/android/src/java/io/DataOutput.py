from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DataOutput"]

class DataOutput(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "java/io/DataOutput"
    write = JavaMultipleMethod([("(I)V", False, False), ("([B)V", False, False), ("([BII)V", False, False)])
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