from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["FormEditRecord"]

class FormEditRecord(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/graphics/pdf/models/FormEditRecord"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    EDIT_TYPE_CLICK = JavaStaticField("I")
    EDIT_TYPE_SET_INDICES = JavaStaticField("I")
    EDIT_TYPE_SET_TEXT = JavaStaticField("I")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getSelectedIndices = JavaMethod("()[I")
    getClickPoint = JavaMethod("()Landroid/graphics/Point;")
    getWidgetIndex = JavaMethod("()I")
    getPageNumber = JavaMethod("()I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    getType = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")
    getText = JavaMethod("()Ljava/lang/String;")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/graphics/pdf/models/FormEditRecord$Builder"
        __javaconstructor__ = [("(III)V", False)]
        setClickPoint = JavaMethod("(Landroid/graphics/Point;)Landroid/graphics/pdf/models/FormEditRecord$Builder;")
        setSelectedIndices = JavaMethod("([I)Landroid/graphics/pdf/models/FormEditRecord$Builder;")
        build = JavaMethod("()Landroid/graphics/pdf/models/FormEditRecord;")
        setText = JavaMethod("(Ljava/lang/String;)Landroid/graphics/pdf/models/FormEditRecord$Builder;")