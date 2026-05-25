from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Edits"]

class Edits(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/icu/text/Edits"
    __javaconstructor__ = [("()V", False)]
    reset = JavaMethod("()V")
    addUnchanged = JavaMethod("(I)V")
    addReplace = JavaMethod("(II)V")
    lengthDelta = JavaMethod("()I")
    hasChanges = JavaMethod("()Z")
    numberOfChanges = JavaMethod("()I")
    getCoarseChangesIterator = JavaMethod("()Landroid/icu/text/Edits$Iterator;")
    getCoarseIterator = JavaMethod("()Landroid/icu/text/Edits$Iterator;")
    getFineChangesIterator = JavaMethod("()Landroid/icu/text/Edits$Iterator;")
    getFineIterator = JavaMethod("()Landroid/icu/text/Edits$Iterator;")
    mergeAndAppend = JavaMethod("(Landroid/icu/text/Edits;Landroid/icu/text/Edits;)Landroid/icu/text/Edits;")

    class Iterator(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/icu/text/Edits/Iterator"
        next = JavaMethod("()Z")
        findSourceIndex = JavaMethod("(I)Z")
        findDestinationIndex = JavaMethod("(I)Z")
        destinationIndexFromSourceIndex = JavaMethod("(I)I")
        sourceIndexFromDestinationIndex = JavaMethod("(I)I")
        hasChange = JavaMethod("()Z")
        oldLength = JavaMethod("()I")
        newLength = JavaMethod("()I")
        sourceIndex = JavaMethod("()I")
        replacementIndex = JavaMethod("()I")
        destinationIndex = JavaMethod("()I")
        toString = JavaMethod("()Ljava/lang/String;")