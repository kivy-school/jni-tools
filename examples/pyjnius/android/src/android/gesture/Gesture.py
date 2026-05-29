from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Gesture"]

class Gesture(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/gesture/Gesture"
    __javaconstructor__ = [("()V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getBoundingBox = JavaMethod("()Landroid/graphics/RectF;")
    getStrokes = JavaMethod("()Ljava/util/ArrayList;")
    addStroke = JavaMethod("(Landroid/gesture/GestureStroke;)V")
    toBitmap = JavaMultipleMethod([("(IIII)Landroid/graphics/Bitmap;", False, False), ("(IIIII)Landroid/graphics/Bitmap;", False, False)])
    getStrokesCount = JavaMethod("()I")
    clone = JavaMethod("()Ljava/lang/Object;")
    getLength = JavaMethod("()F")
    getID = JavaMethod("()J")
    toPath = JavaMultipleMethod([("(Landroid/graphics/Path;)Landroid/graphics/Path;", False, False), ("(IIII)Landroid/graphics/Path;", False, False), ("()Landroid/graphics/Path;", False, False), ("(Landroid/graphics/Path;IIII)Landroid/graphics/Path;", False, False)])
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")