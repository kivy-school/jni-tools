from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["StringBuilder"]

class StringBuilder(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/lang/StringBuilder"
    __javaconstructor__ = [("(Ljava/lang/CharSequence;)V", False), ("(Ljava/lang/String;)V", False), ("(I)V", False), ("()V", False)]
    length = JavaMethod("()I")
    toString = JavaMethod("()Ljava/lang/String;")
    append = JavaMultipleMethod([("(Ljava/lang/StringBuffer;)Ljava/lang/AbstractStringBuilder;", False, False), ("(Ljava/lang/CharSequence;)Ljava/lang/AbstractStringBuilder;", False, False), ("(Ljava/lang/CharSequence;II)Ljava/lang/AbstractStringBuilder;", False, False), ("([C)Ljava/lang/AbstractStringBuilder;", False, False), ("(Ljava/lang/String;)Ljava/lang/AbstractStringBuilder;", False, False), ("(Ljava/lang/Object;)Ljava/lang/AbstractStringBuilder;", False, False), ("(C)Ljava/lang/Appendable;", False, False), ("(I)Ljava/lang/AbstractStringBuilder;", False, False), ("(J)Ljava/lang/AbstractStringBuilder;", False, False), ("(F)Ljava/lang/AbstractStringBuilder;", False, False), ("(D)Ljava/lang/AbstractStringBuilder;", False, False), ("(C)Ljava/lang/AbstractStringBuilder;", False, False), ("(Z)Ljava/lang/AbstractStringBuilder;", False, False), ("([CII)Ljava/lang/AbstractStringBuilder;", False, False), ("(Ljava/lang/CharSequence;)Ljava/lang/StringBuilder;", False, False), ("(Ljava/lang/CharSequence;II)Ljava/lang/StringBuilder;", False, False), ("([C)Ljava/lang/StringBuilder;", False, False), ("([CII)Ljava/lang/StringBuilder;", False, False), ("(Ljava/lang/CharSequence;)Ljava/lang/Appendable;", False, False), ("(Ljava/lang/Object;)Ljava/lang/StringBuilder;", False, False), ("(Ljava/lang/String;)Ljava/lang/StringBuilder;", False, False), ("(Ljava/lang/StringBuffer;)Ljava/lang/StringBuilder;", False, False), ("(J)Ljava/lang/StringBuilder;", False, False), ("(F)Ljava/lang/StringBuilder;", False, False), ("(D)Ljava/lang/StringBuilder;", False, False), ("(Ljava/lang/CharSequence;II)Ljava/lang/Appendable;", False, False), ("(Z)Ljava/lang/StringBuilder;", False, False), ("(C)Ljava/lang/StringBuilder;", False, False), ("(I)Ljava/lang/StringBuilder;", False, False)])
    reverse = JavaMultipleMethod([("()Ljava/lang/StringBuilder;", False, False), ("()Ljava/lang/AbstractStringBuilder;", False, False)])
    getChars = JavaMethod("(II[CI)V")
    compareTo = JavaMultipleMethod([("(Ljava/lang/Object;)I", False, False), ("(Ljava/lang/StringBuilder;)I", False, False)])
    indexOf = JavaMultipleMethod([("(Ljava/lang/String;I)I", False, False), ("(Ljava/lang/String;)I", False, False)])
    insert = JavaMultipleMethod([("(ILjava/lang/CharSequence;)Ljava/lang/StringBuilder;", False, False), ("(ILjava/lang/String;)Ljava/lang/StringBuilder;", False, False), ("(I[C)Ljava/lang/StringBuilder;", False, False), ("(ILjava/lang/CharSequence;)Ljava/lang/AbstractStringBuilder;", False, False), ("(I[C)Ljava/lang/AbstractStringBuilder;", False, False), ("(ILjava/lang/String;)Ljava/lang/AbstractStringBuilder;", False, False), ("(ILjava/lang/Object;)Ljava/lang/AbstractStringBuilder;", False, False), ("(I[CII)Ljava/lang/AbstractStringBuilder;", False, False), ("(II)Ljava/lang/StringBuilder;", False, False), ("(ID)Ljava/lang/StringBuilder;", False, False), ("(IF)Ljava/lang/StringBuilder;", False, False), ("(IJ)Ljava/lang/StringBuilder;", False, False), ("(IC)Ljava/lang/StringBuilder;", False, False), ("(IZ)Ljava/lang/StringBuilder;", False, False), ("(ILjava/lang/CharSequence;II)Ljava/lang/StringBuilder;", False, False), ("(IJ)Ljava/lang/AbstractStringBuilder;", False, False), ("(IF)Ljava/lang/AbstractStringBuilder;", False, False), ("(ID)Ljava/lang/AbstractStringBuilder;", False, False), ("(ILjava/lang/Object;)Ljava/lang/StringBuilder;", False, False), ("(I[CII)Ljava/lang/StringBuilder;", False, False), ("(ILjava/lang/CharSequence;II)Ljava/lang/AbstractStringBuilder;", False, False), ("(IZ)Ljava/lang/AbstractStringBuilder;", False, False), ("(IC)Ljava/lang/AbstractStringBuilder;", False, False), ("(II)Ljava/lang/AbstractStringBuilder;", False, False)])
    charAt = JavaMethod("(I)C")
    codePointAt = JavaMethod("(I)I")
    codePointBefore = JavaMethod("(I)I")
    codePointCount = JavaMethod("(II)I")
    offsetByCodePoints = JavaMethod("(II)I")
    lastIndexOf = JavaMultipleMethod([("(Ljava/lang/String;I)I", False, False), ("(Ljava/lang/String;)I", False, False)])
    substring = JavaMultipleMethod([("(I)Ljava/lang/String;", False, False), ("(II)Ljava/lang/String;", False, False)])
    replace = JavaMultipleMethod([("(IILjava/lang/String;)Ljava/lang/StringBuilder;", False, False), ("(IILjava/lang/String;)Ljava/lang/AbstractStringBuilder;", False, False)])
    repeat = JavaMultipleMethod([("(Ljava/lang/CharSequence;I)Ljava/lang/AbstractStringBuilder;", False, False), ("(II)Ljava/lang/StringBuilder;", False, False), ("(II)Ljava/lang/AbstractStringBuilder;", False, False), ("(Ljava/lang/CharSequence;I)Ljava/lang/StringBuilder;", False, False)])
    codePoints = JavaMethod("()Ljava/util/stream/IntStream;")
    subSequence = JavaMethod("(II)Ljava/lang/CharSequence;")
    chars = JavaMethod("()Ljava/util/stream/IntStream;")
    trimToSize = JavaMethod("()V")
    setLength = JavaMethod("(I)V")
    capacity = JavaMethod("()I")
    ensureCapacity = JavaMethod("(I)V")
    setCharAt = JavaMethod("(IC)V")
    appendCodePoint = JavaMultipleMethod([("(I)Ljava/lang/StringBuilder;", False, False), ("(I)Ljava/lang/AbstractStringBuilder;", False, False)])
    delete = JavaMultipleMethod([("(II)Ljava/lang/AbstractStringBuilder;", False, False), ("(II)Ljava/lang/StringBuilder;", False, False)])
    deleteCharAt = JavaMultipleMethod([("(I)Ljava/lang/StringBuilder;", False, False), ("(I)Ljava/lang/AbstractStringBuilder;", False, False)])