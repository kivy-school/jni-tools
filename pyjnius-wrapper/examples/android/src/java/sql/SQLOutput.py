from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SQLOutput"]

class SQLOutput(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "java/sql/SQLOutput"
    writeString = JavaMethod("(Ljava/lang/String;)V")
    writeBoolean = JavaMethod("(Z)V")
    writeByte = JavaMethod("(B)V")
    writeShort = JavaMethod("(S)V")
    writeInt = JavaMethod("(I)V")
    writeLong = JavaMethod("(J)V")
    writeFloat = JavaMethod("(F)V")
    writeDouble = JavaMethod("(D)V")
    writeBigDecimal = JavaMethod("(Ljava/math/BigDecimal;)V")
    writeBytes = JavaMethod("([B)V")
    writeDate = JavaMethod("(Ljava/sql/Date;)V")
    writeTime = JavaMethod("(Ljava/sql/Time;)V")
    writeTimestamp = JavaMethod("(Ljava/sql/Timestamp;)V")
    writeCharacterStream = JavaMethod("(Ljava/io/Reader;)V")
    writeAsciiStream = JavaMethod("(Ljava/io/InputStream;)V")
    writeBinaryStream = JavaMethod("(Ljava/io/InputStream;)V")
    writeObject = JavaMethod("(Ljava/sql/SQLData;)V")
    writeRef = JavaMethod("(Ljava/sql/Ref;)V")
    writeBlob = JavaMethod("(Ljava/sql/Blob;)V")
    writeClob = JavaMethod("(Ljava/sql/Clob;)V")
    writeStruct = JavaMethod("(Ljava/sql/Struct;)V")
    writeArray = JavaMethod("(Ljava/sql/Array;)V")
    writeURL = JavaMethod("(Ljava/net/URL;)V")
    writeNString = JavaMethod("(Ljava/lang/String;)V")
    writeNClob = JavaMethod("(Ljava/sql/NClob;)V")
    writeRowId = JavaMethod("(Ljava/sql/RowId;)V")
    writeSQLXML = JavaMethod("(Ljava/sql/SQLXML;)V")