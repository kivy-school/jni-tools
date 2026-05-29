from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["StreamTokenizer"]

class StreamTokenizer(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/io/StreamTokenizer"
    __javaconstructor__ = [("(Ljava/io/Reader;)V", False), ("(Ljava/io/InputStream;)V", False)]
    ttype = JavaField("I")
    TT_EOF = JavaStaticField("I")
    TT_EOL = JavaStaticField("I")
    TT_NUMBER = JavaStaticField("I")
    TT_WORD = JavaStaticField("I")
    sval = JavaField("Ljava/lang/String;")
    nval = JavaField("D")
    toString = JavaMethod("()Ljava/lang/String;")
    nextToken = JavaMethod("()I")
    pushBack = JavaMethod("()V")
    wordChars = JavaMethod("(II)V")
    whitespaceChars = JavaMethod("(II)V")
    commentChar = JavaMethod("(I)V")
    quoteChar = JavaMethod("(I)V")
    parseNumbers = JavaMethod("()V")
    resetSyntax = JavaMethod("()V")
    ordinaryChars = JavaMethod("(II)V")
    ordinaryChar = JavaMethod("(I)V")
    eolIsSignificant = JavaMethod("(Z)V")
    slashStarComments = JavaMethod("(Z)V")
    slashSlashComments = JavaMethod("(Z)V")
    lowerCaseMode = JavaMethod("(Z)V")
    lineno = JavaMethod("()I")