from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["FormEditRecord"]

class FormEditRecord(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/graphics/pdf/models/FormEditRecord"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    EDIT_TYPE_CLICK = JavaStaticField("I")
    EDIT_TYPE_SET_INDICES = JavaStaticField("I")
    EDIT_TYPE_SET_TEXT = JavaStaticField("I")
    getPageNumber = JavaMethod("()I")
    getWidgetIndex = JavaMethod("()I")
    getType = JavaMethod("()I")
    getClickPoint = JavaMethod("()Landroid/graphics/Point;")
    getSelectedIndices = JavaMethod("()[I")
    getText = JavaMethod("()Ljava/lang/String;")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/graphics/pdf/models/FormEditRecord/Builder"
        __javaconstructor__ = [("(III)V", False)]
        build = JavaMethod("()Landroid/graphics/pdf/models/FormEditRecord;")
        setClickPoint = JavaMethod("(Landroid/graphics/Point;)Landroid/graphics/pdf/models/FormEditRecord$Builder;")
        setSelectedIndices = JavaMethod("([I)Landroid/graphics/pdf/models/FormEditRecord$Builder;")
        setText = JavaMethod("(Ljava/lang/String;)Landroid/graphics/pdf/models/FormEditRecord$Builder;")