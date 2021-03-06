// Generated by the protocol buffer compiler.  DO NOT EDIT!
// source: secgcs.proto

#define INTERNAL_SUPPRESS_PROTOBUF_FIELD_DEPRECATION
#include "secgcs.pb.h"

#include <algorithm>

#include <google/protobuf/stubs/common.h>
#include <google/protobuf/stubs/once.h>
#include <google/protobuf/io/coded_stream.h>
#include <google/protobuf/wire_format_lite_inl.h>
#include <google/protobuf/descriptor.h>
#include <google/protobuf/generated_message_reflection.h>
#include <google/protobuf/reflection_ops.h>
#include <google/protobuf/wire_format.h>
// @@protoc_insertion_point(includes)

namespace {

const ::google::protobuf::Descriptor* QGCData_descriptor_ = NULL;
const ::google::protobuf::internal::GeneratedMessageReflection*
  QGCData_reflection_ = NULL;

}  // namespace


void protobuf_AssignDesc_secgcs_2eproto() {
  protobuf_AddDesc_secgcs_2eproto();
  const ::google::protobuf::FileDescriptor* file =
    ::google::protobuf::DescriptorPool::generated_pool()->FindFileByName(
      "secgcs.proto");
  GOOGLE_CHECK(file != NULL);
  QGCData_descriptor_ = file->message_type(0);
  static const int QGCData_offsets_[7] = {
    GOOGLE_PROTOBUF_GENERATED_MESSAGE_FIELD_OFFSET(QGCData, msg_type_),
    GOOGLE_PROTOBUF_GENERATED_MESSAGE_FIELD_OFFSET(QGCData, latitude_),
    GOOGLE_PROTOBUF_GENERATED_MESSAGE_FIELD_OFFSET(QGCData, longitude_),
    GOOGLE_PROTOBUF_GENERATED_MESSAGE_FIELD_OFFSET(QGCData, heading_),
    GOOGLE_PROTOBUF_GENERATED_MESSAGE_FIELD_OFFSET(QGCData, altitude_),
    GOOGLE_PROTOBUF_GENERATED_MESSAGE_FIELD_OFFSET(QGCData, outside_temp_),
    GOOGLE_PROTOBUF_GENERATED_MESSAGE_FIELD_OFFSET(QGCData, batt_tmp_),
  };
  QGCData_reflection_ =
    new ::google::protobuf::internal::GeneratedMessageReflection(
      QGCData_descriptor_,
      QGCData::default_instance_,
      QGCData_offsets_,
      GOOGLE_PROTOBUF_GENERATED_MESSAGE_FIELD_OFFSET(QGCData, _has_bits_[0]),
      GOOGLE_PROTOBUF_GENERATED_MESSAGE_FIELD_OFFSET(QGCData, _unknown_fields_),
      -1,
      ::google::protobuf::DescriptorPool::generated_pool(),
      ::google::protobuf::MessageFactory::generated_factory(),
      sizeof(QGCData));
}

namespace {

GOOGLE_PROTOBUF_DECLARE_ONCE(protobuf_AssignDescriptors_once_);
inline void protobuf_AssignDescriptorsOnce() {
  ::google::protobuf::GoogleOnceInit(&protobuf_AssignDescriptors_once_,
                 &protobuf_AssignDesc_secgcs_2eproto);
}

void protobuf_RegisterTypes(const ::std::string&) {
  protobuf_AssignDescriptorsOnce();
  ::google::protobuf::MessageFactory::InternalRegisterGeneratedMessage(
    QGCData_descriptor_, &QGCData::default_instance());
}

}  // namespace

void protobuf_ShutdownFile_secgcs_2eproto() {
  delete QGCData::default_instance_;
  delete QGCData_reflection_;
}

void protobuf_AddDesc_secgcs_2eproto() {
  static bool already_here = false;
  if (already_here) return;
  already_here = true;
  GOOGLE_PROTOBUF_VERIFY_VERSION;

  ::google::protobuf::DescriptorPool::InternalAddGeneratedFile(
    "\n\014secgcs.proto\"\213\001\n\007QGCData\022\020\n\010msg_type\030\001"
    " \002(\t\022\020\n\010latitude\030\002 \002(\001\022\021\n\tlongitude\030\003 \002("
    "\001\022\017\n\007heading\030\004 \002(\001\022\020\n\010altitude\030\005 \002(\001\022\024\n\014"
    "outside_temp\030\006 \001(\005\022\020\n\010batt_tmp\030\007 \001(\005", 156);
  ::google::protobuf::MessageFactory::InternalRegisterGeneratedFile(
    "secgcs.proto", &protobuf_RegisterTypes);
  QGCData::default_instance_ = new QGCData();
  QGCData::default_instance_->InitAsDefaultInstance();
  ::google::protobuf::internal::OnShutdown(&protobuf_ShutdownFile_secgcs_2eproto);
}

// Force AddDescriptors() to be called at static initialization time.
struct StaticDescriptorInitializer_secgcs_2eproto {
  StaticDescriptorInitializer_secgcs_2eproto() {
    protobuf_AddDesc_secgcs_2eproto();
  }
} static_descriptor_initializer_secgcs_2eproto_;

// ===================================================================

#ifndef _MSC_VER
const int QGCData::kMsgTypeFieldNumber;
const int QGCData::kLatitudeFieldNumber;
const int QGCData::kLongitudeFieldNumber;
const int QGCData::kHeadingFieldNumber;
const int QGCData::kAltitudeFieldNumber;
const int QGCData::kOutsideTempFieldNumber;
const int QGCData::kBattTmpFieldNumber;
#endif  // !_MSC_VER

QGCData::QGCData()
  : ::google::protobuf::Message() {
  SharedCtor();
}

void QGCData::InitAsDefaultInstance() {
}

QGCData::QGCData(const QGCData& from)
  : ::google::protobuf::Message() {
  SharedCtor();
  MergeFrom(from);
}

void QGCData::SharedCtor() {
  _cached_size_ = 0;
  msg_type_ = const_cast< ::std::string*>(&::google::protobuf::internal::kEmptyString);
  latitude_ = 0;
  longitude_ = 0;
  heading_ = 0;
  altitude_ = 0;
  outside_temp_ = 0;
  batt_tmp_ = 0;
  ::memset(_has_bits_, 0, sizeof(_has_bits_));
}

QGCData::~QGCData() {
  SharedDtor();
}

void QGCData::SharedDtor() {
  if (msg_type_ != &::google::protobuf::internal::kEmptyString) {
    delete msg_type_;
  }
  if (this != default_instance_) {
  }
}

void QGCData::SetCachedSize(int size) const {
  GOOGLE_SAFE_CONCURRENT_WRITES_BEGIN();
  _cached_size_ = size;
  GOOGLE_SAFE_CONCURRENT_WRITES_END();
}
const ::google::protobuf::Descriptor* QGCData::descriptor() {
  protobuf_AssignDescriptorsOnce();
  return QGCData_descriptor_;
}

const QGCData& QGCData::default_instance() {
  if (default_instance_ == NULL) protobuf_AddDesc_secgcs_2eproto();
  return *default_instance_;
}

QGCData* QGCData::default_instance_ = NULL;

QGCData* QGCData::New() const {
  return new QGCData;
}

void QGCData::Clear() {
  if (_has_bits_[0 / 32] & (0xffu << (0 % 32))) {
    if (has_msg_type()) {
      if (msg_type_ != &::google::protobuf::internal::kEmptyString) {
        msg_type_->clear();
      }
    }
    latitude_ = 0;
    longitude_ = 0;
    heading_ = 0;
    altitude_ = 0;
    outside_temp_ = 0;
    batt_tmp_ = 0;
  }
  ::memset(_has_bits_, 0, sizeof(_has_bits_));
  mutable_unknown_fields()->Clear();
}

bool QGCData::MergePartialFromCodedStream(
    ::google::protobuf::io::CodedInputStream* input) {
#define DO_(EXPRESSION) if (!(EXPRESSION)) return false
  ::google::protobuf::uint32 tag;
  while ((tag = input->ReadTag()) != 0) {
    switch (::google::protobuf::internal::WireFormatLite::GetTagFieldNumber(tag)) {
      // required string msg_type = 1;
      case 1: {
        if (::google::protobuf::internal::WireFormatLite::GetTagWireType(tag) ==
            ::google::protobuf::internal::WireFormatLite::WIRETYPE_LENGTH_DELIMITED) {
          DO_(::google::protobuf::internal::WireFormatLite::ReadString(
                input, this->mutable_msg_type()));
          ::google::protobuf::internal::WireFormat::VerifyUTF8String(
            this->msg_type().data(), this->msg_type().length(),
            ::google::protobuf::internal::WireFormat::PARSE);
        } else {
          goto handle_uninterpreted;
        }
        if (input->ExpectTag(17)) goto parse_latitude;
        break;
      }

      // required double latitude = 2;
      case 2: {
        if (::google::protobuf::internal::WireFormatLite::GetTagWireType(tag) ==
            ::google::protobuf::internal::WireFormatLite::WIRETYPE_FIXED64) {
         parse_latitude:
          DO_((::google::protobuf::internal::WireFormatLite::ReadPrimitive<
                   double, ::google::protobuf::internal::WireFormatLite::TYPE_DOUBLE>(
                 input, &latitude_)));
          set_has_latitude();
        } else {
          goto handle_uninterpreted;
        }
        if (input->ExpectTag(25)) goto parse_longitude;
        break;
      }

      // required double longitude = 3;
      case 3: {
        if (::google::protobuf::internal::WireFormatLite::GetTagWireType(tag) ==
            ::google::protobuf::internal::WireFormatLite::WIRETYPE_FIXED64) {
         parse_longitude:
          DO_((::google::protobuf::internal::WireFormatLite::ReadPrimitive<
                   double, ::google::protobuf::internal::WireFormatLite::TYPE_DOUBLE>(
                 input, &longitude_)));
          set_has_longitude();
        } else {
          goto handle_uninterpreted;
        }
        if (input->ExpectTag(33)) goto parse_heading;
        break;
      }

      // required double heading = 4;
      case 4: {
        if (::google::protobuf::internal::WireFormatLite::GetTagWireType(tag) ==
            ::google::protobuf::internal::WireFormatLite::WIRETYPE_FIXED64) {
         parse_heading:
          DO_((::google::protobuf::internal::WireFormatLite::ReadPrimitive<
                   double, ::google::protobuf::internal::WireFormatLite::TYPE_DOUBLE>(
                 input, &heading_)));
          set_has_heading();
        } else {
          goto handle_uninterpreted;
        }
        if (input->ExpectTag(41)) goto parse_altitude;
        break;
      }

      // required double altitude = 5;
      case 5: {
        if (::google::protobuf::internal::WireFormatLite::GetTagWireType(tag) ==
            ::google::protobuf::internal::WireFormatLite::WIRETYPE_FIXED64) {
         parse_altitude:
          DO_((::google::protobuf::internal::WireFormatLite::ReadPrimitive<
                   double, ::google::protobuf::internal::WireFormatLite::TYPE_DOUBLE>(
                 input, &altitude_)));
          set_has_altitude();
        } else {
          goto handle_uninterpreted;
        }
        if (input->ExpectTag(48)) goto parse_outside_temp;
        break;
      }

      // optional int32 outside_temp = 6;
      case 6: {
        if (::google::protobuf::internal::WireFormatLite::GetTagWireType(tag) ==
            ::google::protobuf::internal::WireFormatLite::WIRETYPE_VARINT) {
         parse_outside_temp:
          DO_((::google::protobuf::internal::WireFormatLite::ReadPrimitive<
                   ::google::protobuf::int32, ::google::protobuf::internal::WireFormatLite::TYPE_INT32>(
                 input, &outside_temp_)));
          set_has_outside_temp();
        } else {
          goto handle_uninterpreted;
        }
        if (input->ExpectTag(56)) goto parse_batt_tmp;
        break;
      }

      // optional int32 batt_tmp = 7;
      case 7: {
        if (::google::protobuf::internal::WireFormatLite::GetTagWireType(tag) ==
            ::google::protobuf::internal::WireFormatLite::WIRETYPE_VARINT) {
         parse_batt_tmp:
          DO_((::google::protobuf::internal::WireFormatLite::ReadPrimitive<
                   ::google::protobuf::int32, ::google::protobuf::internal::WireFormatLite::TYPE_INT32>(
                 input, &batt_tmp_)));
          set_has_batt_tmp();
        } else {
          goto handle_uninterpreted;
        }
        if (input->ExpectAtEnd()) return true;
        break;
      }

      default: {
      handle_uninterpreted:
        if (::google::protobuf::internal::WireFormatLite::GetTagWireType(tag) ==
            ::google::protobuf::internal::WireFormatLite::WIRETYPE_END_GROUP) {
          return true;
        }
        DO_(::google::protobuf::internal::WireFormat::SkipField(
              input, tag, mutable_unknown_fields()));
        break;
      }
    }
  }
  return true;
#undef DO_
}

void QGCData::SerializeWithCachedSizes(
    ::google::protobuf::io::CodedOutputStream* output) const {
  // required string msg_type = 1;
  if (has_msg_type()) {
    ::google::protobuf::internal::WireFormat::VerifyUTF8String(
      this->msg_type().data(), this->msg_type().length(),
      ::google::protobuf::internal::WireFormat::SERIALIZE);
    ::google::protobuf::internal::WireFormatLite::WriteString(
      1, this->msg_type(), output);
  }

  // required double latitude = 2;
  if (has_latitude()) {
    ::google::protobuf::internal::WireFormatLite::WriteDouble(2, this->latitude(), output);
  }

  // required double longitude = 3;
  if (has_longitude()) {
    ::google::protobuf::internal::WireFormatLite::WriteDouble(3, this->longitude(), output);
  }

  // required double heading = 4;
  if (has_heading()) {
    ::google::protobuf::internal::WireFormatLite::WriteDouble(4, this->heading(), output);
  }

  // required double altitude = 5;
  if (has_altitude()) {
    ::google::protobuf::internal::WireFormatLite::WriteDouble(5, this->altitude(), output);
  }

  // optional int32 outside_temp = 6;
  if (has_outside_temp()) {
    ::google::protobuf::internal::WireFormatLite::WriteInt32(6, this->outside_temp(), output);
  }

  // optional int32 batt_tmp = 7;
  if (has_batt_tmp()) {
    ::google::protobuf::internal::WireFormatLite::WriteInt32(7, this->batt_tmp(), output);
  }

  if (!unknown_fields().empty()) {
    ::google::protobuf::internal::WireFormat::SerializeUnknownFields(
        unknown_fields(), output);
  }
}

::google::protobuf::uint8* QGCData::SerializeWithCachedSizesToArray(
    ::google::protobuf::uint8* target) const {
  // required string msg_type = 1;
  if (has_msg_type()) {
    ::google::protobuf::internal::WireFormat::VerifyUTF8String(
      this->msg_type().data(), this->msg_type().length(),
      ::google::protobuf::internal::WireFormat::SERIALIZE);
    target =
      ::google::protobuf::internal::WireFormatLite::WriteStringToArray(
        1, this->msg_type(), target);
  }

  // required double latitude = 2;
  if (has_latitude()) {
    target = ::google::protobuf::internal::WireFormatLite::WriteDoubleToArray(2, this->latitude(), target);
  }

  // required double longitude = 3;
  if (has_longitude()) {
    target = ::google::protobuf::internal::WireFormatLite::WriteDoubleToArray(3, this->longitude(), target);
  }

  // required double heading = 4;
  if (has_heading()) {
    target = ::google::protobuf::internal::WireFormatLite::WriteDoubleToArray(4, this->heading(), target);
  }

  // required double altitude = 5;
  if (has_altitude()) {
    target = ::google::protobuf::internal::WireFormatLite::WriteDoubleToArray(5, this->altitude(), target);
  }

  // optional int32 outside_temp = 6;
  if (has_outside_temp()) {
    target = ::google::protobuf::internal::WireFormatLite::WriteInt32ToArray(6, this->outside_temp(), target);
  }

  // optional int32 batt_tmp = 7;
  if (has_batt_tmp()) {
    target = ::google::protobuf::internal::WireFormatLite::WriteInt32ToArray(7, this->batt_tmp(), target);
  }

  if (!unknown_fields().empty()) {
    target = ::google::protobuf::internal::WireFormat::SerializeUnknownFieldsToArray(
        unknown_fields(), target);
  }
  return target;
}

int QGCData::ByteSize() const {
  int total_size = 0;

  if (_has_bits_[0 / 32] & (0xffu << (0 % 32))) {
    // required string msg_type = 1;
    if (has_msg_type()) {
      total_size += 1 +
        ::google::protobuf::internal::WireFormatLite::StringSize(
          this->msg_type());
    }

    // required double latitude = 2;
    if (has_latitude()) {
      total_size += 1 + 8;
    }

    // required double longitude = 3;
    if (has_longitude()) {
      total_size += 1 + 8;
    }

    // required double heading = 4;
    if (has_heading()) {
      total_size += 1 + 8;
    }

    // required double altitude = 5;
    if (has_altitude()) {
      total_size += 1 + 8;
    }

    // optional int32 outside_temp = 6;
    if (has_outside_temp()) {
      total_size += 1 +
        ::google::protobuf::internal::WireFormatLite::Int32Size(
          this->outside_temp());
    }

    // optional int32 batt_tmp = 7;
    if (has_batt_tmp()) {
      total_size += 1 +
        ::google::protobuf::internal::WireFormatLite::Int32Size(
          this->batt_tmp());
    }

  }
  if (!unknown_fields().empty()) {
    total_size +=
      ::google::protobuf::internal::WireFormat::ComputeUnknownFieldsSize(
        unknown_fields());
  }
  GOOGLE_SAFE_CONCURRENT_WRITES_BEGIN();
  _cached_size_ = total_size;
  GOOGLE_SAFE_CONCURRENT_WRITES_END();
  return total_size;
}

void QGCData::MergeFrom(const ::google::protobuf::Message& from) {
  GOOGLE_CHECK_NE(&from, this);
  const QGCData* source =
    ::google::protobuf::internal::dynamic_cast_if_available<const QGCData*>(
      &from);
  if (source == NULL) {
    ::google::protobuf::internal::ReflectionOps::Merge(from, this);
  } else {
    MergeFrom(*source);
  }
}

void QGCData::MergeFrom(const QGCData& from) {
  GOOGLE_CHECK_NE(&from, this);
  if (from._has_bits_[0 / 32] & (0xffu << (0 % 32))) {
    if (from.has_msg_type()) {
      set_msg_type(from.msg_type());
    }
    if (from.has_latitude()) {
      set_latitude(from.latitude());
    }
    if (from.has_longitude()) {
      set_longitude(from.longitude());
    }
    if (from.has_heading()) {
      set_heading(from.heading());
    }
    if (from.has_altitude()) {
      set_altitude(from.altitude());
    }
    if (from.has_outside_temp()) {
      set_outside_temp(from.outside_temp());
    }
    if (from.has_batt_tmp()) {
      set_batt_tmp(from.batt_tmp());
    }
  }
  mutable_unknown_fields()->MergeFrom(from.unknown_fields());
}

void QGCData::CopyFrom(const ::google::protobuf::Message& from) {
  if (&from == this) return;
  Clear();
  MergeFrom(from);
}

void QGCData::CopyFrom(const QGCData& from) {
  if (&from == this) return;
  Clear();
  MergeFrom(from);
}

bool QGCData::IsInitialized() const {
  if ((_has_bits_[0] & 0x0000001f) != 0x0000001f) return false;

  return true;
}

void QGCData::Swap(QGCData* other) {
  if (other != this) {
    std::swap(msg_type_, other->msg_type_);
    std::swap(latitude_, other->latitude_);
    std::swap(longitude_, other->longitude_);
    std::swap(heading_, other->heading_);
    std::swap(altitude_, other->altitude_);
    std::swap(outside_temp_, other->outside_temp_);
    std::swap(batt_tmp_, other->batt_tmp_);
    std::swap(_has_bits_[0], other->_has_bits_[0]);
    _unknown_fields_.Swap(&other->_unknown_fields_);
    std::swap(_cached_size_, other->_cached_size_);
  }
}

::google::protobuf::Metadata QGCData::GetMetadata() const {
  protobuf_AssignDescriptorsOnce();
  ::google::protobuf::Metadata metadata;
  metadata.descriptor = QGCData_descriptor_;
  metadata.reflection = QGCData_reflection_;
  return metadata;
}


// @@protoc_insertion_point(namespace_scope)

// @@protoc_insertion_point(global_scope)
