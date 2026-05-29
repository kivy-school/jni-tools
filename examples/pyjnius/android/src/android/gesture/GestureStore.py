from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["GestureStore"]

class GestureStore(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/gesture/GestureStore"
    __javaconstructor__ = [("()V", False)]
    ORIENTATION_INVARIANT = JavaStaticField("I")
    ORIENTATION_SENSITIVE = JavaStaticField("I")
    SEQUENCE_INVARIANT = JavaStaticField("I")
    SEQUENCE_SENSITIVE = JavaStaticField("I")
    recognize = JavaMethod("(Landroid/gesture/Gesture;)Ljava/util/ArrayList;")
    addGesture = JavaMethod("(Ljava/lang/String;Landroid/gesture/Gesture;)V")
    setSequenceType = JavaMethod("(I)V")
    getGestureEntries = JavaMethod("()Ljava/util/Set;")
    removeEntry = JavaMethod("(Ljava/lang/String;)V")
    getGestures = JavaMethod("(Ljava/lang/String;)Ljava/util/ArrayList;")
    removeGesture = JavaMethod("(Ljava/lang/String;Landroid/gesture/Gesture;)V")
    getSequenceType = JavaMethod("()I")
    getOrientationStyle = JavaMethod("()I")
    setOrientationStyle = JavaMethod("(I)V")
    load = JavaMultipleMethod([("(Ljava/io/InputStream;Z)V", False, False), ("(Ljava/io/InputStream;)V", False, False)])
    save = JavaMultipleMethod([("(Ljava/io/OutputStream;Z)V", False, False), ("(Ljava/io/OutputStream;)V", False, False)])
    hasChanged = JavaMethod("()Z")