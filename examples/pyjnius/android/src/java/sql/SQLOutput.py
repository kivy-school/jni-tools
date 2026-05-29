from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SQLOutput"]

class SQLOutput(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/sql/SQLOutput"
    writeBigDecimal = JavaMethod("(Ljava/math/BigDecimal;)V")
    writeDate = JavaMethod("(Ljava/sql/Date;)V")
    writeTime = JavaMethod("(Ljava/sql/Time;)V")
    writeTimestamp = JavaMethod("(Ljava/sql/Timestamp;)V")
    writeCharacterStream = JavaMethod("(Ljava/io/Reader;)V")
    writeAsciiStream = JavaMethod("(Ljava/io/InputStream;)V")
    writeBinaryStream = JavaMethod("(Ljava/io/InputStream;)V")
    writeRef = JavaMethod("(Ljava/sql/Ref;)V")
    writeClob = JavaMethod("(Ljava/sql/Clob;)V")
    writeStruct = JavaMethod("(Ljava/sql/Struct;)V")
    writeURL = JavaMethod("(Ljava/net/URL;)V")
    writeNString = JavaMethod("(Ljava/lang/String;)V")
    writeNClob = JavaMethod("(Ljava/sql/NClob;)V")
    writeRowId = JavaMethod("(Ljava/sql/RowId;)V")
    writeSQLXML = JavaMethod("(Ljava/sql/SQLXML;)V")
    writeObject = JavaMultipleMethod([("(Ljava/sql/SQLData;)V", False, False), ("(Ljava/lang/Object;Ljava/sql/SQLType;)V", False, False)])
    writeInt = JavaMethod("(I)V")
    writeBytes = JavaMethod("([B)V")
    writeFloat = JavaMethod("(F)V")
    writeBlob = JavaMethod("(Ljava/sql/Blob;)V")
    writeArray = JavaMethod("(Ljava/sql/Array;)V")
    writeLong = JavaMethod("(J)V")
    writeByte = JavaMethod("(B)V")
    writeShort = JavaMethod("(S)V")
    writeString = JavaMethod("(Ljava/lang/String;)V")
    writeBoolean = JavaMethod("(Z)V")
    writeDouble = JavaMethod("(D)V")