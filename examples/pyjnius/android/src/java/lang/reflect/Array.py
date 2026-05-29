from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Array"]

class Array(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/lang/reflect/Array"
    getLength = JavaStaticMethod("(Ljava/lang/Object;)I")
    getBoolean = JavaStaticMethod("(Ljava/lang/Object;I)Z")
    getByte = JavaStaticMethod("(Ljava/lang/Object;I)B")
    getShort = JavaStaticMethod("(Ljava/lang/Object;I)S")
    getChar = JavaStaticMethod("(Ljava/lang/Object;I)C")
    getInt = JavaStaticMethod("(Ljava/lang/Object;I)I")
    getLong = JavaStaticMethod("(Ljava/lang/Object;I)J")
    getFloat = JavaStaticMethod("(Ljava/lang/Object;I)F")
    getDouble = JavaStaticMethod("(Ljava/lang/Object;I)D")
    get = JavaStaticMethod("(Ljava/lang/Object;I)Ljava/lang/Object;")
    newInstance = JavaMultipleMethod([("(Ljava/lang/Class;I)Ljava/lang/Object;", True, False), ("(Ljava/lang/Class;[I)Ljava/lang/Object;", True, True)])
    set = JavaStaticMethod("(Ljava/lang/Object;ILjava/lang/Object;)V")
    setBoolean = JavaStaticMethod("(Ljava/lang/Object;IZ)V")
    setByte = JavaStaticMethod("(Ljava/lang/Object;IB)V")
    setChar = JavaStaticMethod("(Ljava/lang/Object;IC)V")
    setShort = JavaStaticMethod("(Ljava/lang/Object;IS)V")
    setInt = JavaStaticMethod("(Ljava/lang/Object;II)V")
    setLong = JavaStaticMethod("(Ljava/lang/Object;IJ)V")
    setFloat = JavaStaticMethod("(Ljava/lang/Object;IF)V")
    setDouble = JavaStaticMethod("(Ljava/lang/Object;ID)V")