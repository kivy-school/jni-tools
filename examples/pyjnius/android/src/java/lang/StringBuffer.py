from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["StringBuffer"]

class StringBuffer(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/lang/StringBuffer"
    __javaconstructor__ = [("(Ljava/lang/CharSequence;)V", False), ("(Ljava/lang/String;)V", False), ("(I)V", False), ("()V", False)]
    length = JavaMethod("()I")
    toString = JavaMethod("()Ljava/lang/String;")
    append = JavaMultipleMethod([("([C)Ljava/lang/AbstractStringBuilder;", False, False), ("(I)Ljava/lang/StringBuffer;", False, False), ("(J)Ljava/lang/StringBuffer;", False, False), ("(F)Ljava/lang/StringBuffer;", False, False), ("([C)Ljava/lang/StringBuffer;", False, False), ("([CII)Ljava/lang/StringBuffer;", False, False), ("(Z)Ljava/lang/StringBuffer;", False, False), ("(C)Ljava/lang/StringBuffer;", False, False), ("(I)Ljava/lang/AbstractStringBuilder;", False, False), ("(J)Ljava/lang/AbstractStringBuilder;", False, False), ("(F)Ljava/lang/AbstractStringBuilder;", False, False), ("(D)Ljava/lang/AbstractStringBuilder;", False, False), ("(D)Ljava/lang/StringBuffer;", False, False), ("([CII)Ljava/lang/AbstractStringBuilder;", False, False), ("(Z)Ljava/lang/AbstractStringBuilder;", False, False), ("(C)Ljava/lang/AbstractStringBuilder;", False, False), ("(Ljava/lang/String;)Ljava/lang/AbstractStringBuilder;", False, False), ("(Ljava/lang/StringBuffer;)Ljava/lang/AbstractStringBuilder;", False, False), ("(Ljava/lang/CharSequence;)Ljava/lang/AbstractStringBuilder;", False, False), ("(Ljava/lang/CharSequence;)Ljava/lang/Appendable;", False, False), ("(Ljava/lang/CharSequence;II)Ljava/lang/Appendable;", False, False), ("(C)Ljava/lang/Appendable;", False, False), ("(Ljava/lang/Object;)Ljava/lang/AbstractStringBuilder;", False, False), ("(Ljava/lang/String;)Ljava/lang/StringBuffer;", False, False), ("(Ljava/lang/StringBuffer;)Ljava/lang/StringBuffer;", False, False), ("(Ljava/lang/CharSequence;)Ljava/lang/StringBuffer;", False, False), ("(Ljava/lang/CharSequence;II)Ljava/lang/StringBuffer;", False, False), ("(Ljava/lang/CharSequence;II)Ljava/lang/AbstractStringBuilder;", False, False), ("(Ljava/lang/Object;)Ljava/lang/StringBuffer;", False, False)])
    reverse = JavaMultipleMethod([("()Ljava/lang/StringBuffer;", False, False), ("()Ljava/lang/AbstractStringBuilder;", False, False)])
    getChars = JavaMethod("(II[CI)V")
    compareTo = JavaMultipleMethod([("(Ljava/lang/StringBuffer;)I", False, False), ("(Ljava/lang/Object;)I", False, False)])
    indexOf = JavaMultipleMethod([("(Ljava/lang/String;I)I", False, False), ("(Ljava/lang/String;)I", False, False)])
    insert = JavaMultipleMethod([("(IJ)Ljava/lang/AbstractStringBuilder;", False, False), ("(II)Ljava/lang/AbstractStringBuilder;", False, False), ("(IC)Ljava/lang/AbstractStringBuilder;", False, False), ("(IZ)Ljava/lang/AbstractStringBuilder;", False, False), ("(IF)Ljava/lang/AbstractStringBuilder;", False, False), ("(ID)Ljava/lang/AbstractStringBuilder;", False, False), ("(ILjava/lang/Object;)Ljava/lang/StringBuffer;", False, False), ("(ILjava/lang/String;)Ljava/lang/AbstractStringBuilder;", False, False), ("(ILjava/lang/Object;)Ljava/lang/AbstractStringBuilder;", False, False), ("(I[CII)Ljava/lang/AbstractStringBuilder;", False, False), ("(I[CII)Ljava/lang/StringBuffer;", False, False), ("(I[C)Ljava/lang/AbstractStringBuilder;", False, False), ("(ILjava/lang/CharSequence;)Ljava/lang/AbstractStringBuilder;", False, False), ("(ILjava/lang/CharSequence;II)Ljava/lang/AbstractStringBuilder;", False, False), ("(I[C)Ljava/lang/StringBuffer;", False, False), ("(IF)Ljava/lang/StringBuffer;", False, False), ("(IJ)Ljava/lang/StringBuffer;", False, False), ("(ILjava/lang/String;)Ljava/lang/StringBuffer;", False, False), ("(ILjava/lang/CharSequence;)Ljava/lang/StringBuffer;", False, False), ("(ILjava/lang/CharSequence;II)Ljava/lang/StringBuffer;", False, False), ("(IZ)Ljava/lang/StringBuffer;", False, False), ("(ID)Ljava/lang/StringBuffer;", False, False), ("(IC)Ljava/lang/StringBuffer;", False, False), ("(II)Ljava/lang/StringBuffer;", False, False)])
    charAt = JavaMethod("(I)C")
    codePointAt = JavaMethod("(I)I")
    codePointBefore = JavaMethod("(I)I")
    codePointCount = JavaMethod("(II)I")
    offsetByCodePoints = JavaMethod("(II)I")
    lastIndexOf = JavaMultipleMethod([("(Ljava/lang/String;I)I", False, False), ("(Ljava/lang/String;)I", False, False)])
    substring = JavaMultipleMethod([("(I)Ljava/lang/String;", False, False), ("(II)Ljava/lang/String;", False, False)])
    replace = JavaMultipleMethod([("(IILjava/lang/String;)Ljava/lang/StringBuffer;", False, False), ("(IILjava/lang/String;)Ljava/lang/AbstractStringBuilder;", False, False)])
    repeat = JavaMultipleMethod([("(Ljava/lang/CharSequence;I)Ljava/lang/AbstractStringBuilder;", False, False), ("(II)Ljava/lang/AbstractStringBuilder;", False, False), ("(Ljava/lang/CharSequence;I)Ljava/lang/StringBuffer;", False, False), ("(II)Ljava/lang/StringBuffer;", False, False)])
    codePoints = JavaMethod("()Ljava/util/stream/IntStream;")
    subSequence = JavaMethod("(II)Ljava/lang/CharSequence;")
    chars = JavaMethod("()Ljava/util/stream/IntStream;")
    trimToSize = JavaMethod("()V")
    setLength = JavaMethod("(I)V")
    capacity = JavaMethod("()I")
    ensureCapacity = JavaMethod("(I)V")
    setCharAt = JavaMethod("(IC)V")
    appendCodePoint = JavaMultipleMethod([("(I)Ljava/lang/AbstractStringBuilder;", False, False), ("(I)Ljava/lang/StringBuffer;", False, False)])
    delete = JavaMultipleMethod([("(II)Ljava/lang/StringBuffer;", False, False), ("(II)Ljava/lang/AbstractStringBuilder;", False, False)])
    deleteCharAt = JavaMultipleMethod([("(I)Ljava/lang/StringBuffer;", False, False), ("(I)Ljava/lang/AbstractStringBuilder;", False, False)])