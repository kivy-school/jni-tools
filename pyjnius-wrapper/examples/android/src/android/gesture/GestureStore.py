from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["GestureStore"]

class GestureStore(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/gesture/GestureStore"
    __javaconstructor__ = [("()V", False)]
    ORIENTATION_INVARIANT = JavaStaticField("I")
    ORIENTATION_SENSITIVE = JavaStaticField("I")
    SEQUENCE_INVARIANT = JavaStaticField("I")
    SEQUENCE_SENSITIVE = JavaStaticField("I")
    setOrientationStyle = JavaMethod("(I)V")
    getOrientationStyle = JavaMethod("()I")
    setSequenceType = JavaMethod("(I)V")
    getSequenceType = JavaMethod("()I")
    getGestureEntries = JavaMethod("()Ljava/util/Set;")
    recognize = JavaMethod("(Landroid/gesture/Gesture;)Ljava/util/ArrayList;")
    addGesture = JavaMethod("(Ljava/lang/String;Landroid/gesture/Gesture;)V")
    removeGesture = JavaMethod("(Ljava/lang/String;Landroid/gesture/Gesture;)V")
    removeEntry = JavaMethod("(Ljava/lang/String;)V")
    getGestures = JavaMethod("(Ljava/lang/String;)Ljava/util/ArrayList;")
    hasChanged = JavaMethod("()Z")
    save = JavaMultipleMethod([("(Ljava/io/OutputStream;)V", False, False), ("(Ljava/io/OutputStream;Z)V", False, False)])
    load = JavaMultipleMethod([("(Ljava/io/InputStream;)V", False, False), ("(Ljava/io/InputStream;Z)V", False, False)])