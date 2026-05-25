from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["GestureLibrary"]

class GestureLibrary(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/gesture/GestureLibrary"
    __javaconstructor__ = [("()V", False)]
    mStore = JavaField("Landroid/gesture/GestureStore;")
    save = JavaMethod("()Z")
    load = JavaMethod("()Z")
    isReadOnly = JavaMethod("()Z")
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