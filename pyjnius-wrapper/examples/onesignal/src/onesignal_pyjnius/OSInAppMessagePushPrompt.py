from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["OSInAppMessagePushPrompt"]

class OSInAppMessagePushPrompt(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/OSInAppMessagePushPrompt"
    __javaconstructor__ = [("()V", False)]