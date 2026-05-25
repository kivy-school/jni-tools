from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SQLInput"]

class SQLInput(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "java/sql/SQLInput"
    readString = JavaMethod("()Ljava/lang/String;")
    readBoolean = JavaMethod("()Z")
    readByte = JavaMethod("()B")
    readShort = JavaMethod("()S")
    readInt = JavaMethod("()I")
    readLong = JavaMethod("()J")
    readFloat = JavaMethod("()F")
    readDouble = JavaMethod("()D")
    readBigDecimal = JavaMethod("()Ljava/math/BigDecimal;")
    readBytes = JavaMethod("()[B")
    readDate = JavaMethod("()Ljava/sql/Date;")
    readTime = JavaMethod("()Ljava/sql/Time;")
    readTimestamp = JavaMethod("()Ljava/sql/Timestamp;")
    readCharacterStream = JavaMethod("()Ljava/io/Reader;")
    readAsciiStream = JavaMethod("()Ljava/io/InputStream;")
    readBinaryStream = JavaMethod("()Ljava/io/InputStream;")
    readObject = JavaMethod("()Ljava/lang/Object;")
    readRef = JavaMethod("()Ljava/sql/Ref;")
    readBlob = JavaMethod("()Ljava/sql/Blob;")
    readClob = JavaMethod("()Ljava/sql/Clob;")
    readArray = JavaMethod("()Ljava/sql/Array;")
    wasNull = JavaMethod("()Z")
    readURL = JavaMethod("()Ljava/net/URL;")
    readNClob = JavaMethod("()Ljava/sql/NClob;")
    readNString = JavaMethod("()Ljava/lang/String;")
    readSQLXML = JavaMethod("()Ljava/sql/SQLXML;")
    readRowId = JavaMethod("()Ljava/sql/RowId;")