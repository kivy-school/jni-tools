from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["StringBuffer"]

class StringBuffer(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/lang/StringBuffer"
    __javaconstructor__ = [("()V", False), ("(I)V", False), ("(Ljava/lang/String;)V", False), ("(Ljava/lang/CharSequence;)V", False)]
    compareTo = JavaMethod("(Ljava/lang/StringBuffer;)I")
    length = JavaMethod("()I")
    capacity = JavaMethod("()I")
    ensureCapacity = JavaMethod("(I)V")
    trimToSize = JavaMethod("()V")
    setLength = JavaMethod("(I)V")
    charAt = JavaMethod("(I)C")
    codePointAt = JavaMethod("(I)I")
    codePointBefore = JavaMethod("(I)I")
    codePointCount = JavaMethod("(II)I")
    offsetByCodePoints = JavaMethod("(II)I")
    getChars = JavaMethod("(II[CI)V")
    setCharAt = JavaMethod("(IC)V")
    append = JavaMultipleMethod([("(Ljava/lang/Object;)Ljava/lang/StringBuffer;", False, False), ("(Ljava/lang/String;)Ljava/lang/StringBuffer;", False, False), ("(Ljava/lang/StringBuffer;)Ljava/lang/StringBuffer;", False, False), ("(Ljava/lang/CharSequence;)Ljava/lang/StringBuffer;", False, False), ("(Ljava/lang/CharSequence;II)Ljava/lang/StringBuffer;", False, False), ("([C)Ljava/lang/StringBuffer;", False, False), ("([CII)Ljava/lang/StringBuffer;", False, False), ("(Z)Ljava/lang/StringBuffer;", False, False), ("(C)Ljava/lang/StringBuffer;", False, False), ("(I)Ljava/lang/StringBuffer;", False, False), ("(J)Ljava/lang/StringBuffer;", False, False), ("(F)Ljava/lang/StringBuffer;", False, False), ("(D)Ljava/lang/StringBuffer;", False, False)])
    appendCodePoint = JavaMethod("(I)Ljava/lang/StringBuffer;")
    delete = JavaMethod("(II)Ljava/lang/StringBuffer;")
    deleteCharAt = JavaMethod("(I)Ljava/lang/StringBuffer;")
    replace = JavaMethod("(IILjava/lang/String;)Ljava/lang/StringBuffer;")
    substring = JavaMultipleMethod([("(I)Ljava/lang/String;", False, False), ("(II)Ljava/lang/String;", False, False)])
    subSequence = JavaMethod("(II)Ljava/lang/CharSequence;")
    insert = JavaMultipleMethod([("(I[CII)Ljava/lang/StringBuffer;", False, False), ("(ILjava/lang/Object;)Ljava/lang/StringBuffer;", False, False), ("(ILjava/lang/String;)Ljava/lang/StringBuffer;", False, False), ("(I[C)Ljava/lang/StringBuffer;", False, False), ("(ILjava/lang/CharSequence;)Ljava/lang/StringBuffer;", False, False), ("(ILjava/lang/CharSequence;II)Ljava/lang/StringBuffer;", False, False), ("(IZ)Ljava/lang/StringBuffer;", False, False), ("(IC)Ljava/lang/StringBuffer;", False, False), ("(II)Ljava/lang/StringBuffer;", False, False), ("(IJ)Ljava/lang/StringBuffer;", False, False), ("(IF)Ljava/lang/StringBuffer;", False, False), ("(ID)Ljava/lang/StringBuffer;", False, False)])
    indexOf = JavaMultipleMethod([("(Ljava/lang/String;)I", False, False), ("(Ljava/lang/String;I)I", False, False)])
    lastIndexOf = JavaMultipleMethod([("(Ljava/lang/String;)I", False, False), ("(Ljava/lang/String;I)I", False, False)])
    reverse = JavaMethod("()Ljava/lang/StringBuffer;")
    toString = JavaMethod("()Ljava/lang/String;")
    chars = JavaMethod("()Ljava/util/stream/IntStream;")
    codePoints = JavaMethod("()Ljava/util/stream/IntStream;")