from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["MtpEvent"]

class MtpEvent(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/mtp/MtpEvent"
    EVENT_CANCEL_TRANSACTION = JavaStaticField("I")
    EVENT_CAPTURE_COMPLETE = JavaStaticField("I")
    EVENT_DEVICE_INFO_CHANGED = JavaStaticField("I")
    EVENT_DEVICE_PROP_CHANGED = JavaStaticField("I")
    EVENT_DEVICE_RESET = JavaStaticField("I")
    EVENT_OBJECT_ADDED = JavaStaticField("I")
    EVENT_OBJECT_INFO_CHANGED = JavaStaticField("I")
    EVENT_OBJECT_PROP_CHANGED = JavaStaticField("I")
    EVENT_OBJECT_PROP_DESC_CHANGED = JavaStaticField("I")
    EVENT_OBJECT_REFERENCES_CHANGED = JavaStaticField("I")
    EVENT_OBJECT_REMOVED = JavaStaticField("I")
    EVENT_REQUEST_OBJECT_TRANSFER = JavaStaticField("I")
    EVENT_STORAGE_INFO_CHANGED = JavaStaticField("I")
    EVENT_STORE_ADDED = JavaStaticField("I")
    EVENT_STORE_FULL = JavaStaticField("I")
    EVENT_STORE_REMOVED = JavaStaticField("I")
    EVENT_UNDEFINED = JavaStaticField("I")
    EVENT_UNREPORTED_STATUS = JavaStaticField("I")
    getStorageId = JavaMethod("()I")
    getObjectHandle = JavaMethod("()I")
    getDevicePropCode = JavaMethod("()I")
    getEventCode = JavaMethod("()I")
    getObjectFormatCode = JavaMethod("()I")
    getObjectPropCode = JavaMethod("()I")
    getParameter1 = JavaMethod("()I")
    getParameter2 = JavaMethod("()I")
    getParameter3 = JavaMethod("()I")
    getTransactionId = JavaMethod("()I")