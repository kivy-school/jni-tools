from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["StreamTokenizer"]

class StreamTokenizer(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/io/StreamTokenizer"
    __javaconstructor__ = [("(Ljava/io/InputStream;)V", False), ("(Ljava/io/Reader;)V", False)]
    TT_EOF = JavaStaticField("I")
    TT_EOL = JavaStaticField("I")
    TT_NUMBER = JavaStaticField("I")
    TT_WORD = JavaStaticField("I")
    nval = JavaField("D")
    sval = JavaField("Ljava/lang/String;")
    ttype = JavaField("I")
    resetSyntax = JavaMethod("()V")
    wordChars = JavaMethod("(II)V")
    whitespaceChars = JavaMethod("(II)V")
    ordinaryChars = JavaMethod("(II)V")
    ordinaryChar = JavaMethod("(I)V")
    commentChar = JavaMethod("(I)V")
    quoteChar = JavaMethod("(I)V")
    parseNumbers = JavaMethod("()V")
    eolIsSignificant = JavaMethod("(Z)V")
    slashStarComments = JavaMethod("(Z)V")
    slashSlashComments = JavaMethod("(Z)V")
    lowerCaseMode = JavaMethod("(Z)V")
    nextToken = JavaMethod("()I")
    pushBack = JavaMethod("()V")
    lineno = JavaMethod("()I")
    toString = JavaMethod("()Ljava/lang/String;")