from typing import Any, ClassVar, overload
from java.nio.Buffer import Buffer
from java.nio.FloatBuffer import FloatBuffer
from java.nio.IntBuffer import IntBuffer
from java.nio.ShortBuffer import ShortBuffer

class GLES11Ext:
    GL_3DC_XY_AMD: ClassVar[int]
    GL_3DC_X_AMD: ClassVar[int]
    GL_ATC_RGBA_EXPLICIT_ALPHA_AMD: ClassVar[int]
    GL_ATC_RGBA_INTERPOLATED_ALPHA_AMD: ClassVar[int]
    GL_ATC_RGB_AMD: ClassVar[int]
    GL_BGRA: ClassVar[int]
    GL_BLEND_DST_ALPHA_OES: ClassVar[int]
    GL_BLEND_DST_RGB_OES: ClassVar[int]
    GL_BLEND_EQUATION_ALPHA_OES: ClassVar[int]
    GL_BLEND_EQUATION_OES: ClassVar[int]
    GL_BLEND_EQUATION_RGB_OES: ClassVar[int]
    GL_BLEND_SRC_ALPHA_OES: ClassVar[int]
    GL_BLEND_SRC_RGB_OES: ClassVar[int]
    GL_BUFFER_ACCESS_OES: ClassVar[int]
    GL_BUFFER_MAPPED_OES: ClassVar[int]
    GL_BUFFER_MAP_POINTER_OES: ClassVar[int]
    GL_COLOR_ATTACHMENT0_OES: ClassVar[int]
    GL_CURRENT_PALETTE_MATRIX_OES: ClassVar[int]
    GL_DECR_WRAP_OES: ClassVar[int]
    GL_DEPTH24_STENCIL8_OES: ClassVar[int]
    GL_DEPTH_ATTACHMENT_OES: ClassVar[int]
    GL_DEPTH_COMPONENT16_OES: ClassVar[int]
    GL_DEPTH_COMPONENT24_OES: ClassVar[int]
    GL_DEPTH_COMPONENT32_OES: ClassVar[int]
    GL_DEPTH_STENCIL_OES: ClassVar[int]
    GL_ETC1_RGB8_OES: ClassVar[int]
    GL_FIXED_OES: ClassVar[int]
    GL_FRAMEBUFFER_ATTACHMENT_OBJECT_NAME_OES: ClassVar[int]
    GL_FRAMEBUFFER_ATTACHMENT_OBJECT_TYPE_OES: ClassVar[int]
    GL_FRAMEBUFFER_ATTACHMENT_TEXTURE_CUBE_MAP_FACE_OES: ClassVar[int]
    GL_FRAMEBUFFER_ATTACHMENT_TEXTURE_LEVEL_OES: ClassVar[int]
    GL_FRAMEBUFFER_BINDING_OES: ClassVar[int]
    GL_FRAMEBUFFER_COMPLETE_OES: ClassVar[int]
    GL_FRAMEBUFFER_INCOMPLETE_ATTACHMENT_OES: ClassVar[int]
    GL_FRAMEBUFFER_INCOMPLETE_DIMENSIONS_OES: ClassVar[int]
    GL_FRAMEBUFFER_INCOMPLETE_FORMATS_OES: ClassVar[int]
    GL_FRAMEBUFFER_INCOMPLETE_MISSING_ATTACHMENT_OES: ClassVar[int]
    GL_FRAMEBUFFER_OES: ClassVar[int]
    GL_FRAMEBUFFER_UNSUPPORTED_OES: ClassVar[int]
    GL_FUNC_ADD_OES: ClassVar[int]
    GL_FUNC_REVERSE_SUBTRACT_OES: ClassVar[int]
    GL_FUNC_SUBTRACT_OES: ClassVar[int]
    GL_INCR_WRAP_OES: ClassVar[int]
    GL_INVALID_FRAMEBUFFER_OPERATION_OES: ClassVar[int]
    GL_MATRIX_INDEX_ARRAY_BUFFER_BINDING_OES: ClassVar[int]
    GL_MATRIX_INDEX_ARRAY_OES: ClassVar[int]
    GL_MATRIX_INDEX_ARRAY_POINTER_OES: ClassVar[int]
    GL_MATRIX_INDEX_ARRAY_SIZE_OES: ClassVar[int]
    GL_MATRIX_INDEX_ARRAY_STRIDE_OES: ClassVar[int]
    GL_MATRIX_INDEX_ARRAY_TYPE_OES: ClassVar[int]
    GL_MATRIX_PALETTE_OES: ClassVar[int]
    GL_MAX_CUBE_MAP_TEXTURE_SIZE_OES: ClassVar[int]
    GL_MAX_PALETTE_MATRICES_OES: ClassVar[int]
    GL_MAX_RENDERBUFFER_SIZE_OES: ClassVar[int]
    GL_MAX_TEXTURE_MAX_ANISOTROPY_EXT: ClassVar[int]
    GL_MAX_VERTEX_UNITS_OES: ClassVar[int]
    GL_MIRRORED_REPEAT_OES: ClassVar[int]
    GL_MODELVIEW_MATRIX_FLOAT_AS_INT_BITS_OES: ClassVar[int]
    GL_NONE_OES: ClassVar[int]
    GL_NORMAL_MAP_OES: ClassVar[int]
    GL_PROJECTION_MATRIX_FLOAT_AS_INT_BITS_OES: ClassVar[int]
    GL_REFLECTION_MAP_OES: ClassVar[int]
    GL_RENDERBUFFER_ALPHA_SIZE_OES: ClassVar[int]
    GL_RENDERBUFFER_BINDING_OES: ClassVar[int]
    GL_RENDERBUFFER_BLUE_SIZE_OES: ClassVar[int]
    GL_RENDERBUFFER_DEPTH_SIZE_OES: ClassVar[int]
    GL_RENDERBUFFER_GREEN_SIZE_OES: ClassVar[int]
    GL_RENDERBUFFER_HEIGHT_OES: ClassVar[int]
    GL_RENDERBUFFER_INTERNAL_FORMAT_OES: ClassVar[int]
    GL_RENDERBUFFER_OES: ClassVar[int]
    GL_RENDERBUFFER_RED_SIZE_OES: ClassVar[int]
    GL_RENDERBUFFER_STENCIL_SIZE_OES: ClassVar[int]
    GL_RENDERBUFFER_WIDTH_OES: ClassVar[int]
    GL_REQUIRED_TEXTURE_IMAGE_UNITS_OES: ClassVar[int]
    GL_RGB565_OES: ClassVar[int]
    GL_RGB5_A1_OES: ClassVar[int]
    GL_RGB8_OES: ClassVar[int]
    GL_RGBA4_OES: ClassVar[int]
    GL_RGBA8_OES: ClassVar[int]
    GL_SAMPLER_EXTERNAL_OES: ClassVar[int]
    GL_STENCIL_ATTACHMENT_OES: ClassVar[int]
    GL_STENCIL_INDEX1_OES: ClassVar[int]
    GL_STENCIL_INDEX4_OES: ClassVar[int]
    GL_STENCIL_INDEX8_OES: ClassVar[int]
    GL_TEXTURE_BINDING_CUBE_MAP_OES: ClassVar[int]
    GL_TEXTURE_BINDING_EXTERNAL_OES: ClassVar[int]
    GL_TEXTURE_CROP_RECT_OES: ClassVar[int]
    GL_TEXTURE_CUBE_MAP_NEGATIVE_X_OES: ClassVar[int]
    GL_TEXTURE_CUBE_MAP_NEGATIVE_Y_OES: ClassVar[int]
    GL_TEXTURE_CUBE_MAP_NEGATIVE_Z_OES: ClassVar[int]
    GL_TEXTURE_CUBE_MAP_OES: ClassVar[int]
    GL_TEXTURE_CUBE_MAP_POSITIVE_X_OES: ClassVar[int]
    GL_TEXTURE_CUBE_MAP_POSITIVE_Y_OES: ClassVar[int]
    GL_TEXTURE_CUBE_MAP_POSITIVE_Z_OES: ClassVar[int]
    GL_TEXTURE_EXTERNAL_OES: ClassVar[int]
    GL_TEXTURE_GEN_MODE_OES: ClassVar[int]
    GL_TEXTURE_GEN_STR_OES: ClassVar[int]
    GL_TEXTURE_MATRIX_FLOAT_AS_INT_BITS_OES: ClassVar[int]
    GL_TEXTURE_MAX_ANISOTROPY_EXT: ClassVar[int]
    GL_UNSIGNED_INT_24_8_OES: ClassVar[int]
    GL_WEIGHT_ARRAY_BUFFER_BINDING_OES: ClassVar[int]
    GL_WEIGHT_ARRAY_OES: ClassVar[int]
    GL_WEIGHT_ARRAY_POINTER_OES: ClassVar[int]
    GL_WEIGHT_ARRAY_SIZE_OES: ClassVar[int]
    GL_WEIGHT_ARRAY_STRIDE_OES: ClassVar[int]
    GL_WEIGHT_ARRAY_TYPE_OES: ClassVar[int]
    GL_WRITE_ONLY_OES: ClassVar[int]
    def __init__(self) -> None: ...
    @staticmethod
    def glBlendEquationSeparateOES(arg0: int, arg1: int) -> None: ...
    @staticmethod
    def glBlendFuncSeparateOES(arg0: int, arg1: int, arg2: int, arg3: int) -> None: ...
    @staticmethod
    def glBlendEquationOES(arg0: int) -> None: ...
    @staticmethod
    def glDrawTexsOES(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> None: ...
    @staticmethod
    def glDrawTexiOES(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> None: ...
    @staticmethod
    def glDrawTexxOES(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> None: ...
    @overload
    @staticmethod
    def glDrawTexsvOES(arg0: list[int], arg1: int) -> None: ...
    @overload
    @staticmethod
    def glDrawTexsvOES(arg0: ShortBuffer) -> None: ...
    @overload
    @staticmethod
    def glDrawTexivOES(arg0: list[int], arg1: int) -> None: ...
    @overload
    @staticmethod
    def glDrawTexivOES(arg0: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glDrawTexxvOES(arg0: list[int], arg1: int) -> None: ...
    @overload
    @staticmethod
    def glDrawTexxvOES(arg0: IntBuffer) -> None: ...
    @staticmethod
    def glDrawTexfOES(arg0: float, arg1: float, arg2: float, arg3: float, arg4: float) -> None: ...
    @overload
    @staticmethod
    def glDrawTexfvOES(arg0: list[float], arg1: int) -> None: ...
    @overload
    @staticmethod
    def glDrawTexfvOES(arg0: FloatBuffer) -> None: ...
    @staticmethod
    def glEGLImageTargetTexture2DOES(arg0: int, arg1: Buffer) -> None: ...
    @staticmethod
    def glEGLImageTargetRenderbufferStorageOES(arg0: int, arg1: Buffer) -> None: ...
    @staticmethod
    def glAlphaFuncxOES(arg0: int, arg1: int) -> None: ...
    @staticmethod
    def glClearColorxOES(arg0: int, arg1: int, arg2: int, arg3: int) -> None: ...
    @staticmethod
    def glClearDepthxOES(arg0: int) -> None: ...
    @overload
    @staticmethod
    def glClipPlanexOES(arg0: int, arg1: list[int], arg2: int) -> None: ...
    @overload
    @staticmethod
    def glClipPlanexOES(arg0: int, arg1: IntBuffer) -> None: ...
    @staticmethod
    def glColor4xOES(arg0: int, arg1: int, arg2: int, arg3: int) -> None: ...
    @staticmethod
    def glDepthRangexOES(arg0: int, arg1: int) -> None: ...
    @staticmethod
    def glFogxOES(arg0: int, arg1: int) -> None: ...
    @overload
    @staticmethod
    def glFogxvOES(arg0: int, arg1: list[int], arg2: int) -> None: ...
    @overload
    @staticmethod
    def glFogxvOES(arg0: int, arg1: IntBuffer) -> None: ...
    @staticmethod
    def glFrustumxOES(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> None: ...
    @overload
    @staticmethod
    def glGetClipPlanexOES(arg0: int, arg1: list[int], arg2: int) -> None: ...
    @overload
    @staticmethod
    def glGetClipPlanexOES(arg0: int, arg1: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glGetFixedvOES(arg0: int, arg1: list[int], arg2: int) -> None: ...
    @overload
    @staticmethod
    def glGetFixedvOES(arg0: int, arg1: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glGetLightxvOES(arg0: int, arg1: int, arg2: list[int], arg3: int) -> None: ...
    @overload
    @staticmethod
    def glGetLightxvOES(arg0: int, arg1: int, arg2: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glGetMaterialxvOES(arg0: int, arg1: int, arg2: list[int], arg3: int) -> None: ...
    @overload
    @staticmethod
    def glGetMaterialxvOES(arg0: int, arg1: int, arg2: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glGetTexEnvxvOES(arg0: int, arg1: int, arg2: list[int], arg3: int) -> None: ...
    @overload
    @staticmethod
    def glGetTexEnvxvOES(arg0: int, arg1: int, arg2: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glGetTexParameterxvOES(arg0: int, arg1: int, arg2: list[int], arg3: int) -> None: ...
    @overload
    @staticmethod
    def glGetTexParameterxvOES(arg0: int, arg1: int, arg2: IntBuffer) -> None: ...
    @staticmethod
    def glLightModelxOES(arg0: int, arg1: int) -> None: ...
    @overload
    @staticmethod
    def glLightModelxvOES(arg0: int, arg1: list[int], arg2: int) -> None: ...
    @overload
    @staticmethod
    def glLightModelxvOES(arg0: int, arg1: IntBuffer) -> None: ...
    @staticmethod
    def glLightxOES(arg0: int, arg1: int, arg2: int) -> None: ...
    @overload
    @staticmethod
    def glLightxvOES(arg0: int, arg1: int, arg2: list[int], arg3: int) -> None: ...
    @overload
    @staticmethod
    def glLightxvOES(arg0: int, arg1: int, arg2: IntBuffer) -> None: ...
    @staticmethod
    def glLineWidthxOES(arg0: int) -> None: ...
    @overload
    @staticmethod
    def glLoadMatrixxOES(arg0: list[int], arg1: int) -> None: ...
    @overload
    @staticmethod
    def glLoadMatrixxOES(arg0: IntBuffer) -> None: ...
    @staticmethod
    def glMaterialxOES(arg0: int, arg1: int, arg2: int) -> None: ...
    @overload
    @staticmethod
    def glMaterialxvOES(arg0: int, arg1: int, arg2: list[int], arg3: int) -> None: ...
    @overload
    @staticmethod
    def glMaterialxvOES(arg0: int, arg1: int, arg2: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glMultMatrixxOES(arg0: list[int], arg1: int) -> None: ...
    @overload
    @staticmethod
    def glMultMatrixxOES(arg0: IntBuffer) -> None: ...
    @staticmethod
    def glMultiTexCoord4xOES(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> None: ...
    @staticmethod
    def glNormal3xOES(arg0: int, arg1: int, arg2: int) -> None: ...
    @staticmethod
    def glOrthoxOES(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> None: ...
    @staticmethod
    def glPointParameterxOES(arg0: int, arg1: int) -> None: ...
    @overload
    @staticmethod
    def glPointParameterxvOES(arg0: int, arg1: list[int], arg2: int) -> None: ...
    @overload
    @staticmethod
    def glPointParameterxvOES(arg0: int, arg1: IntBuffer) -> None: ...
    @staticmethod
    def glPointSizexOES(arg0: int) -> None: ...
    @staticmethod
    def glPolygonOffsetxOES(arg0: int, arg1: int) -> None: ...
    @staticmethod
    def glRotatexOES(arg0: int, arg1: int, arg2: int, arg3: int) -> None: ...
    @staticmethod
    def glSampleCoveragexOES(arg0: int, arg1: bool) -> None: ...
    @staticmethod
    def glScalexOES(arg0: int, arg1: int, arg2: int) -> None: ...
    @staticmethod
    def glTexEnvxOES(arg0: int, arg1: int, arg2: int) -> None: ...
    @overload
    @staticmethod
    def glTexEnvxvOES(arg0: int, arg1: int, arg2: list[int], arg3: int) -> None: ...
    @overload
    @staticmethod
    def glTexEnvxvOES(arg0: int, arg1: int, arg2: IntBuffer) -> None: ...
    @staticmethod
    def glTexParameterxOES(arg0: int, arg1: int, arg2: int) -> None: ...
    @overload
    @staticmethod
    def glTexParameterxvOES(arg0: int, arg1: int, arg2: list[int], arg3: int) -> None: ...
    @overload
    @staticmethod
    def glTexParameterxvOES(arg0: int, arg1: int, arg2: IntBuffer) -> None: ...
    @staticmethod
    def glTranslatexOES(arg0: int, arg1: int, arg2: int) -> None: ...
    @staticmethod
    def glIsRenderbufferOES(arg0: int) -> bool: ...
    @staticmethod
    def glBindRenderbufferOES(arg0: int, arg1: int) -> None: ...
    @overload
    @staticmethod
    def glDeleteRenderbuffersOES(arg0: int, arg1: list[int], arg2: int) -> None: ...
    @overload
    @staticmethod
    def glDeleteRenderbuffersOES(arg0: int, arg1: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glGenRenderbuffersOES(arg0: int, arg1: list[int], arg2: int) -> None: ...
    @overload
    @staticmethod
    def glGenRenderbuffersOES(arg0: int, arg1: IntBuffer) -> None: ...
    @staticmethod
    def glRenderbufferStorageOES(arg0: int, arg1: int, arg2: int, arg3: int) -> None: ...
    @overload
    @staticmethod
    def glGetRenderbufferParameterivOES(arg0: int, arg1: int, arg2: list[int], arg3: int) -> None: ...
    @overload
    @staticmethod
    def glGetRenderbufferParameterivOES(arg0: int, arg1: int, arg2: IntBuffer) -> None: ...
    @staticmethod
    def glIsFramebufferOES(arg0: int) -> bool: ...
    @staticmethod
    def glBindFramebufferOES(arg0: int, arg1: int) -> None: ...
    @overload
    @staticmethod
    def glDeleteFramebuffersOES(arg0: int, arg1: list[int], arg2: int) -> None: ...
    @overload
    @staticmethod
    def glDeleteFramebuffersOES(arg0: int, arg1: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glGenFramebuffersOES(arg0: int, arg1: list[int], arg2: int) -> None: ...
    @overload
    @staticmethod
    def glGenFramebuffersOES(arg0: int, arg1: IntBuffer) -> None: ...
    @staticmethod
    def glCheckFramebufferStatusOES(arg0: int) -> int: ...
    @staticmethod
    def glFramebufferRenderbufferOES(arg0: int, arg1: int, arg2: int, arg3: int) -> None: ...
    @staticmethod
    def glFramebufferTexture2DOES(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> None: ...
    @overload
    @staticmethod
    def glGetFramebufferAttachmentParameterivOES(arg0: int, arg1: int, arg2: int, arg3: list[int], arg4: int) -> None: ...
    @overload
    @staticmethod
    def glGetFramebufferAttachmentParameterivOES(arg0: int, arg1: int, arg2: int, arg3: IntBuffer) -> None: ...
    @staticmethod
    def glGenerateMipmapOES(arg0: int) -> None: ...
    @staticmethod
    def glCurrentPaletteMatrixOES(arg0: int) -> None: ...
    @staticmethod
    def glLoadPaletteFromModelViewMatrixOES() -> None: ...
    @staticmethod
    def glMatrixIndexPointerOES(arg0: int, arg1: int, arg2: int, arg3: Buffer) -> None: ...
    @staticmethod
    def glWeightPointerOES(arg0: int, arg1: int, arg2: int, arg3: Buffer) -> None: ...
    @staticmethod
    def glDepthRangefOES(arg0: float, arg1: float) -> None: ...
    @staticmethod
    def glFrustumfOES(arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float) -> None: ...
    @staticmethod
    def glOrthofOES(arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float) -> None: ...
    @overload
    @staticmethod
    def glClipPlanefOES(arg0: int, arg1: list[float], arg2: int) -> None: ...
    @overload
    @staticmethod
    def glClipPlanefOES(arg0: int, arg1: FloatBuffer) -> None: ...
    @overload
    @staticmethod
    def glGetClipPlanefOES(arg0: int, arg1: list[float], arg2: int) -> None: ...
    @overload
    @staticmethod
    def glGetClipPlanefOES(arg0: int, arg1: FloatBuffer) -> None: ...
    @staticmethod
    def glClearDepthfOES(arg0: float) -> None: ...
    @staticmethod
    def glTexGenfOES(arg0: int, arg1: int, arg2: float) -> None: ...
    @overload
    @staticmethod
    def glTexGenfvOES(arg0: int, arg1: int, arg2: list[float], arg3: int) -> None: ...
    @overload
    @staticmethod
    def glTexGenfvOES(arg0: int, arg1: int, arg2: FloatBuffer) -> None: ...
    @staticmethod
    def glTexGeniOES(arg0: int, arg1: int, arg2: int) -> None: ...
    @overload
    @staticmethod
    def glTexGenivOES(arg0: int, arg1: int, arg2: list[int], arg3: int) -> None: ...
    @overload
    @staticmethod
    def glTexGenivOES(arg0: int, arg1: int, arg2: IntBuffer) -> None: ...
    @staticmethod
    def glTexGenxOES(arg0: int, arg1: int, arg2: int) -> None: ...
    @overload
    @staticmethod
    def glTexGenxvOES(arg0: int, arg1: int, arg2: list[int], arg3: int) -> None: ...
    @overload
    @staticmethod
    def glTexGenxvOES(arg0: int, arg1: int, arg2: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glGetTexGenfvOES(arg0: int, arg1: int, arg2: list[float], arg3: int) -> None: ...
    @overload
    @staticmethod
    def glGetTexGenfvOES(arg0: int, arg1: int, arg2: FloatBuffer) -> None: ...
    @overload
    @staticmethod
    def glGetTexGenivOES(arg0: int, arg1: int, arg2: list[int], arg3: int) -> None: ...
    @overload
    @staticmethod
    def glGetTexGenivOES(arg0: int, arg1: int, arg2: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glGetTexGenxvOES(arg0: int, arg1: int, arg2: list[int], arg3: int) -> None: ...
    @overload
    @staticmethod
    def glGetTexGenxvOES(arg0: int, arg1: int, arg2: IntBuffer) -> None: ...
