from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["FillEventHistory"]

class FillEventHistory(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/service/autofill/FillEventHistory"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    getClientState = JavaMethod("()Landroid/os/Bundle;")
    getEvents = JavaMethod("()Ljava/util/List;")
    toString = JavaMethod("()Ljava/lang/String;")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")

    class Event(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/service/autofill/FillEventHistory/Event"
        NO_SAVE_UI_REASON_DATASET_MATCH = JavaStaticField("I")
        NO_SAVE_UI_REASON_FIELD_VALIDATION_FAILED = JavaStaticField("I")
        NO_SAVE_UI_REASON_HAS_EMPTY_REQUIRED = JavaStaticField("I")
        NO_SAVE_UI_REASON_NONE = JavaStaticField("I")
        NO_SAVE_UI_REASON_NO_SAVE_INFO = JavaStaticField("I")
        NO_SAVE_UI_REASON_NO_VALUE_CHANGED = JavaStaticField("I")
        NO_SAVE_UI_REASON_WITH_DELAY_SAVE_FLAG = JavaStaticField("I")
        TYPE_AUTHENTICATION_SELECTED = JavaStaticField("I")
        TYPE_CONTEXT_COMMITTED = JavaStaticField("I")
        TYPE_DATASETS_SHOWN = JavaStaticField("I")
        TYPE_DATASET_AUTHENTICATION_SELECTED = JavaStaticField("I")
        TYPE_DATASET_SELECTED = JavaStaticField("I")
        TYPE_SAVE_SHOWN = JavaStaticField("I")
        TYPE_VIEW_REQUESTED_AUTOFILL = JavaStaticField("I")
        UI_TYPE_DIALOG = JavaStaticField("I")
        UI_TYPE_INLINE = JavaStaticField("I")
        UI_TYPE_MENU = JavaStaticField("I")
        UI_TYPE_UNKNOWN = JavaStaticField("I")
        getType = JavaMethod("()I")
        getDatasetId = JavaMethod("()Ljava/lang/String;")
        getClientState = JavaMethod("()Landroid/os/Bundle;")
        getSelectedDatasetIds = JavaMethod("()Ljava/util/Set;")
        getIgnoredDatasetIds = JavaMethod("()Ljava/util/Set;")
        getChangedFields = JavaMethod("()Ljava/util/Map;")
        getFieldsClassification = JavaMethod("()Ljava/util/Map;")
        getManuallyEnteredField = JavaMethod("()Ljava/util/Map;")
        getNoSaveUiReason = JavaMethod("()I")
        getUiType = JavaMethod("()I")
        toString = JavaMethod("()Ljava/lang/String;")