from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Edits"]

class Edits(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/icu/text/Edits"
    __javaconstructor__ = [("()V", False)]
    lengthDelta = JavaMethod("()I")
    mergeAndAppend = JavaMethod("(Landroid/icu/text/Edits;Landroid/icu/text/Edits;)Landroid/icu/text/Edits;")
    numberOfChanges = JavaMethod("()I")
    getFineIterator = JavaMethod("()Landroid/icu/text/Edits$Iterator;")
    addReplace = JavaMethod("(II)V")
    getCoarseChangesIterator = JavaMethod("()Landroid/icu/text/Edits$Iterator;")
    getFineChangesIterator = JavaMethod("()Landroid/icu/text/Edits$Iterator;")
    hasChanges = JavaMethod("()Z")
    getCoarseIterator = JavaMethod("()Landroid/icu/text/Edits$Iterator;")
    addUnchanged = JavaMethod("(I)V")
    reset = JavaMethod("()V")

    class Iterator(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/icu/text/Edits$Iterator"
        findSourceIndex = JavaMethod("(I)Z")
        destinationIndex = JavaMethod("()I")
        destinationIndexFromSourceIndex = JavaMethod("(I)I")
        findDestinationIndex = JavaMethod("(I)Z")
        hasChange = JavaMethod("()Z")
        replacementIndex = JavaMethod("()I")
        sourceIndexFromDestinationIndex = JavaMethod("(I)I")
        toString = JavaMethod("()Ljava/lang/String;")
        next = JavaMethod("()Z")
        newLength = JavaMethod("()I")
        oldLength = JavaMethod("()I")
        sourceIndex = JavaMethod("()I")