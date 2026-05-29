from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["WindowId"]

class WindowId(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/WindowId"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    isFocused = JavaMethod("()Z")
    registerFocusObserver = JavaMethod("(Landroid/view/WindowId$FocusObserver;)V")
    unregisterFocusObserver = JavaMethod("(Landroid/view/WindowId$FocusObserver;)V")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    toString = JavaMethod("()Ljava/lang/String;")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")

    class FocusObserver(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/view/WindowId/FocusObserver"
        __javaconstructor__ = [("()V", False)]
        onFocusGained = JavaMethod("(Landroid/view/WindowId;)V")
        onFocusLost = JavaMethod("(Landroid/view/WindowId;)V")