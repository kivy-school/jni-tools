from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["GestureLibrary"]

class GestureLibrary(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/gesture/GestureLibrary"
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
    load = JavaMethod("()Z")
    save = JavaMethod("()Z")
    isReadOnly = JavaMethod("()Z")