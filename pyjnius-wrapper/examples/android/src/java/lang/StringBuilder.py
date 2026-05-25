from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["StringBuilder"]

class StringBuilder(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/lang/StringBuilder"
    __javaconstructor__ = [("()V", False), ("(I)V", False), ("(Ljava/lang/String;)V", False), ("(Ljava/lang/CharSequence;)V", False)]
    compareTo = JavaMethod("(Ljava/lang/StringBuilder;)I")
    append = JavaMultipleMethod([("(Ljava/lang/Object;)Ljava/lang/StringBuilder;", False, False), ("(Ljava/lang/String;)Ljava/lang/StringBuilder;", False, False), ("(Ljava/lang/StringBuffer;)Ljava/lang/StringBuilder;", False, False), ("(Ljava/lang/CharSequence;)Ljava/lang/StringBuilder;", False, False), ("(Ljava/lang/CharSequence;II)Ljava/lang/StringBuilder;", False, False), ("([C)Ljava/lang/StringBuilder;", False, False), ("([CII)Ljava/lang/StringBuilder;", False, False), ("(Z)Ljava/lang/StringBuilder;", False, False), ("(C)Ljava/lang/StringBuilder;", False, False), ("(I)Ljava/lang/StringBuilder;", False, False), ("(J)Ljava/lang/StringBuilder;", False, False), ("(F)Ljava/lang/StringBuilder;", False, False), ("(D)Ljava/lang/StringBuilder;", False, False)])
    appendCodePoint = JavaMethod("(I)Ljava/lang/StringBuilder;")
    delete = JavaMethod("(II)Ljava/lang/StringBuilder;")
    deleteCharAt = JavaMethod("(I)Ljava/lang/StringBuilder;")
    replace = JavaMethod("(IILjava/lang/String;)Ljava/lang/StringBuilder;")
    insert = JavaMultipleMethod([("(I[CII)Ljava/lang/StringBuilder;", False, False), ("(ILjava/lang/Object;)Ljava/lang/StringBuilder;", False, False), ("(ILjava/lang/String;)Ljava/lang/StringBuilder;", False, False), ("(I[C)Ljava/lang/StringBuilder;", False, False), ("(ILjava/lang/CharSequence;)Ljava/lang/StringBuilder;", False, False), ("(ILjava/lang/CharSequence;II)Ljava/lang/StringBuilder;", False, False), ("(IZ)Ljava/lang/StringBuilder;", False, False), ("(IC)Ljava/lang/StringBuilder;", False, False), ("(II)Ljava/lang/StringBuilder;", False, False), ("(IJ)Ljava/lang/StringBuilder;", False, False), ("(IF)Ljava/lang/StringBuilder;", False, False), ("(ID)Ljava/lang/StringBuilder;", False, False)])
    indexOf = JavaMultipleMethod([("(Ljava/lang/String;)I", False, False), ("(Ljava/lang/String;I)I", False, False)])
    lastIndexOf = JavaMultipleMethod([("(Ljava/lang/String;)I", False, False), ("(Ljava/lang/String;I)I", False, False)])
    reverse = JavaMethod("()Ljava/lang/StringBuilder;")
    toString = JavaMethod("()Ljava/lang/String;")
    trimToSize = JavaMethod("()V")
    codePointAt = JavaMethod("(I)I")
    getChars = JavaMethod("(II[CI)V")
    length = JavaMethod("()I")
    setCharAt = JavaMethod("(IC)V")
    subSequence = JavaMethod("(II)Ljava/lang/CharSequence;")
    substring = JavaMultipleMethod([("(I)Ljava/lang/String;", False, False), ("(II)Ljava/lang/String;", False, False)])
    capacity = JavaMethod("()I")
    setLength = JavaMethod("(I)V")
    ensureCapacity = JavaMethod("(I)V")
    codePointBefore = JavaMethod("(I)I")
    charAt = JavaMethod("(I)C")
    codePointCount = JavaMethod("(II)I")
    offsetByCodePoints = JavaMethod("(II)I")
    chars = JavaMethod("()Ljava/util/stream/IntStream;")
    codePoints = JavaMethod("()Ljava/util/stream/IntStream;")