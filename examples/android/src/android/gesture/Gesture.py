from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Gesture"]

class Gesture(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/gesture/Gesture"
    __javaconstructor__ = [("()V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    clone = JavaMethod("()Ljava/lang/Object;")
    getStrokes = JavaMethod("()Ljava/util/ArrayList;")
    getStrokesCount = JavaMethod("()I")
    addStroke = JavaMethod("(Landroid/gesture/GestureStroke;)V")
    getLength = JavaMethod("()F")
    getBoundingBox = JavaMethod("()Landroid/graphics/RectF;")
    toPath = JavaMultipleMethod([("()Landroid/graphics/Path;", False, False), ("(Landroid/graphics/Path;)Landroid/graphics/Path;", False, False), ("(IIII)Landroid/graphics/Path;", False, False), ("(Landroid/graphics/Path;IIII)Landroid/graphics/Path;", False, False)])
    getID = JavaMethod("()J")
    toBitmap = JavaMultipleMethod([("(IIIII)Landroid/graphics/Bitmap;", False, False), ("(IIII)Landroid/graphics/Bitmap;", False, False)])
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")