from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SQLInput"]

class SQLInput(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/sql/SQLInput"
    readBigDecimal = JavaMethod("()Ljava/math/BigDecimal;")
    readDate = JavaMethod("()Ljava/sql/Date;")
    readTime = JavaMethod("()Ljava/sql/Time;")
    readTimestamp = JavaMethod("()Ljava/sql/Timestamp;")
    readCharacterStream = JavaMethod("()Ljava/io/Reader;")
    readAsciiStream = JavaMethod("()Ljava/io/InputStream;")
    readBinaryStream = JavaMethod("()Ljava/io/InputStream;")
    readRef = JavaMethod("()Ljava/sql/Ref;")
    readClob = JavaMethod("()Ljava/sql/Clob;")
    wasNull = JavaMethod("()Z")
    readURL = JavaMethod("()Ljava/net/URL;")
    readNClob = JavaMethod("()Ljava/sql/NClob;")
    readNString = JavaMethod("()Ljava/lang/String;")
    readSQLXML = JavaMethod("()Ljava/sql/SQLXML;")
    readRowId = JavaMethod("()Ljava/sql/RowId;")
    readObject = JavaMultipleMethod([("()Ljava/lang/Object;", False, False), ("(Ljava/lang/Class;)Ljava/lang/Object;", False, False)])
    readInt = JavaMethod("()I")
    readBytes = JavaMethod("()[B")
    readFloat = JavaMethod("()F")
    readBlob = JavaMethod("()Ljava/sql/Blob;")
    readArray = JavaMethod("()Ljava/sql/Array;")
    readLong = JavaMethod("()J")
    readByte = JavaMethod("()B")
    readShort = JavaMethod("()S")
    readString = JavaMethod("()Ljava/lang/String;")
    readBoolean = JavaMethod("()Z")
    readDouble = JavaMethod("()D")