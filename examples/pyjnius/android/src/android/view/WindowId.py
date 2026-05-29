from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["WindowId"]

class WindowId(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/WindowId"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    registerFocusObserver = JavaMethod("(Landroid/view/WindowId$FocusObserver;)V")
    unregisterFocusObserver = JavaMethod("(Landroid/view/WindowId$FocusObserver;)V")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    isFocused = JavaMethod("()Z")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")

    class FocusObserver(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/view/WindowId$FocusObserver"
        __javaconstructor__ = [("()V", False)]
        onFocusLost = JavaMethod("(Landroid/view/WindowId;)V")
        onFocusGained = JavaMethod("(Landroid/view/WindowId;)V")