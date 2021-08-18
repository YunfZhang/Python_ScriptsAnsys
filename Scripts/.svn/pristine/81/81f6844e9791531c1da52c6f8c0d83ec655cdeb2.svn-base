###########################################################
## util Class
###########################################################
package ChangeSynergy::util;

use strict;
use vars qw{$port $protocol $host $queryConfigType $reportConfigType};
use CGI::Util;
use ChangeSynergy::Globals;

sub setPort
{
	$port = shift;
}

sub setProtocol
{
	$protocol = shift;
}

sub setHost
{
	$host = shift;
}

sub setReportConfigType
{
	$reportConfigType = shift;
}

sub setQueryConfigType
{
	$queryConfigType = shift;
}

sub QueryHtmlBase
{
	my $aUser			= shift;
	my $actionFlag		= shift;
	my $reportName		= shift;
	my $queryString		= shift;
	my $queryName		= shift;
	my $reportTitle		= shift;
	my $templateName	= shift;
	my $attributeList	= shift;

	return(new ChangeSynergy::apiData(ChangeSynergy::util::QueryHtmlBaseStr($aUser, $actionFlag, $reportName, $queryString, $queryName,
										$reportTitle, $templateName, $attributeList)));
}

sub QueryHtmlBaseStr
{
	my $aUser			= shift;
	my $actionFlag		= shift;
	my $reportName		= shift;
	my $queryString		= shift;
	my $queryName		= shift;
	my $reportTitle		= shift;
	my $templateName	= shift;
	my $attributeList	= shift;
	my $xmlData			= "";

	if(!defined($aUser))
	{
		die "User information object is undef";
	}

	$xmlData .= "<csapi_token>"			. $aUser->getUserToken()	. "</csapi_token>";
	$xmlData .= "<csapi_role>"			. $aUser->getUserRole()		. "</csapi_role>";
	$xmlData .= "<csapi_database>"		. $aUser->getUserDatabase()	. "</csapi_database>";
	$xmlData .= "<csapi_user>"			. $aUser->getUserName()		. "</csapi_user>";
	$xmlData .= "<csapi_action_flag>"	. $actionFlag				. "</csapi_action_flag>";
	$xmlData .= "<csapi_chosen_report>"	. xmlEncode($reportName)	. "</csapi_chosen_report>";

	if(defined($queryString))
	{
		$xmlData .= "<csapi_query_string>" . xmlEncode($queryString) . "</csapi_query_string>";
	}

	if(defined($templateName))
	{
		$xmlData .= "<csapi_template_flag>" . $templateName . "</csapi_template_flag>";
	}

	if(defined($queryName))
	{
		$xmlData .= "<csapi_chosen_query>" . xmlEncode($queryName) . "</csapi_chosen_query>";
	}

	if(defined($reportTitle))
	{
		$xmlData .= "<csapi_report_title>" . xmlEncode($reportTitle) . "</csapi_report_title>";
	}

	if(defined($attributeList))
	{
		$xmlData .= "<csapi_attribute_list>" . $attributeList . "</csapi_attribute_list>";
	}
	
	if(defined($reportConfigType))
	{
		$xmlData .= "<csapi_report_config_type>" . $reportConfigType . "</csapi_report_config_type>";
	}
	
	if(defined($queryConfigType))
	{
		$xmlData .= "<csapi_query_config_type>" . $queryConfigType . "</csapi_query_config_type>";
	}

	return(ChangeSynergy::util::callCsapi($aUser, $xmlData));
}

sub ModifyShowAction
{
	my $aUser			= shift;
	my $lpData			= shift;
	my $actFlag			= shift;

	my $xmlData			= "";
	my $tmp				= $lpData->toShowXml();

	$xmlData .= "<csapi_action_flag>"	. $actFlag					. "</csapi_action_flag>";
	$xmlData .= "<csapi_token>"			. $aUser->getUserToken()	. "</csapi_token>";
	$xmlData .= "<csapi_role>"			. $aUser->getUserRole()		. "</csapi_role>";
	$xmlData .= "<csapi_database>"		. $aUser->getUserDatabase() . "</csapi_database>";
	$xmlData .= "<csapi_user>"			. $aUser->getUserName()		. "</csapi_user>";
	$xmlData .= "<csapi_request_data>"	. $tmp						. "</csapi_request_data>";

	return(ChangeSynergy::util::callCsapi($aUser, $xmlData));
}

sub ModifySubmitAction
{
	my $aUser			= shift;
	my $lpData			= shift;
	my $actFlag			= shift;

	my $xmlData			= "";
	my $tmp				= $lpData->toSubmitXml();

	$xmlData .= "<csapi_action_flag>"	. $actFlag					. "</csapi_action_flag>";
	$xmlData .= "<csapi_token>"			. $aUser->getUserToken()	. "</csapi_token>";
	$xmlData .= "<csapi_role>"			. $aUser->getUserRole()		. "</csapi_role>";
	$xmlData .= "<csapi_database>"		. $aUser->getUserDatabase() . "</csapi_database>";
	$xmlData .= "<csapi_user>"			. $aUser->getUserName()		. "</csapi_user>";
	$xmlData .= "<csapi_request_data>"	. $tmp						. "</csapi_request_data>";

	return(ChangeSynergy::util::callCsapi($aUser, $xmlData));
}

sub ModifySubmitAssocAction
{
	my $aUser			= shift;
	my $lpData			= shift;
	my $actFlag			= shift;
	my $relationName	= shift;
	my $problemNumber	= shift;

	my $xmlData			= "";
	my $tmp				= $lpData->toSubmitXml();

	$xmlData .= "<csapi_action_flag>"	. $actFlag					. "</csapi_action_flag>";
	$xmlData .= "<csapi_token>"			. $aUser->getUserToken()	. "</csapi_token>";
	$xmlData .= "<csapi_role>"			. $aUser->getUserRole()		. "</csapi_role>";
	$xmlData .= "<csapi_database>"		. $aUser->getUserDatabase() . "</csapi_database>";
	$xmlData .= "<csapi_user>"			. $aUser->getUserName()		. "</csapi_user>";
	$xmlData .= "<csapi_relation_flag>"	. $relationName				. "</csapi_relation_flag>";
	$xmlData .= "<csapi_cr_id>"			. $problemNumber			. "</csapi_cr_id>";
	$xmlData .= "<csapi_request_data>"	. $tmp						. "</csapi_request_data>";

	return(ChangeSynergy::util::callCsapi($aUser, $xmlData));
}

sub AdminAction
{
	my $aUser			= shift;
	my $actFlag			= shift;
	my $actItem			= shift;
	
	my $xmlData			= "";

	if(defined($actItem))
	{
		$xmlData .= "<csapi_action_item>" . $actItem . "</csapi_action_item>";
	}

	$xmlData .= "<csapi_action_flag>"	. $actFlag					. "</csapi_action_flag>";
	$xmlData .= "<csapi_token>"			. $aUser->getUserToken()	. "</csapi_token>";
	$xmlData .= "<csapi_role>"			. $aUser->getUserRole()		. "</csapi_role>";
	$xmlData .= "<csapi_database>"		. $aUser->getUserDatabase() . "</csapi_database>";
	$xmlData .= "<csapi_user>"			. $aUser->getUserName()		. "</csapi_user>";

	return(new ChangeSynergy::apiData(ChangeSynergy::util::callCsapi($aUser, $xmlData)));
}

sub ConfigAdminAction
{
	my $aUser                                       = shift;
	my $actFlag                                     = shift;
	
	my $actBalance_transaction_server               = shift;
	my $actLoad_database_listboxes                  = shift;
	my $actLoad_all_configuration_files             = shift;
	my $actLoad_all_merged_configuration_files      = shift;
	my $actClear_busy_sessions                      = shift;
	my $actReset_ccm_roots_system_tokens            = shift;
	my $actClear_user_configuration_data_structures = shift;
	my $actClear_the_transition_users               = shift;
	my $actReset_configuration_data_load_time       = shift;
	my $actReset_LDAP_pool                          = shift;
	my $actReload_string_table                      = shift;
	my $actLoad_a_specific_configuration_file       = shift;
	
	my $actThe_specific_configuration_file          = shift;

	my $xmlData	= "";

	$xmlData .= "<csapi_action_flag>" . $actFlag                  . "</csapi_action_flag>";
	$xmlData .= "<csapi_token>"       . $aUser->getUserToken()    . "</csapi_token>";
	$xmlData .= "<csapi_role>"        . $aUser->getUserRole()     . "</csapi_role>";
	$xmlData .= "<csapi_database>"    . $aUser->getUserDatabase() . "</csapi_database>";
	$xmlData .= "<csapi_user>"        . $aUser->getUserName()     . "</csapi_user>";

	$xmlData .= "<csapi_balance_transaction_server>"               . $actBalance_transaction_server               . "</csapi_balance_transaction_server>";
	$xmlData .= "<csapi_load_database_listboxes>"                  . $actLoad_database_listboxes                  . "</csapi_load_database_listboxes>";
	$xmlData .= "<csapi_load_all_configuration_files>"             . $actLoad_all_configuration_files             . "</csapi_load_all_configuration_files>";
	$xmlData .= "<csapi_load_all_merged_configuration_files>"      . $actLoad_all_merged_configuration_files      . "</csapi_load_all_merged_configuration_files>";
	$xmlData .= "<csapi_clear_busy_sessions>"                      . $actClear_busy_sessions                      . "</csapi_clear_busy_sessions>";
	$xmlData .= "<csapi_reset_ccm_roots_system_tokens>"            . $actReset_ccm_roots_system_tokens            . "</csapi_reset_ccm_roots_system_tokens>";
	$xmlData .= "<csapi_clear_user_configuration_data_structures>" . $actClear_user_configuration_data_structures . "</csapi_clear_user_configuration_data_structures>";
	$xmlData .= "<csapi_clear_the_transition_users>"               . $actClear_the_transition_users               . "</csapi_clear_the_transition_users>";
	$xmlData .= "<csapi_reset_configuration_data_load_time>"       . $actReset_configuration_data_load_time       . "</csapi_reset_configuration_data_load_time>";
	$xmlData .= "<csapi_reset_ldap_pool>"                          . $actReset_LDAP_pool                          . "</csapi_reset_ldap_pool>";
	$xmlData .= "<csapi_reload_string_table>"                      . $actReload_string_table                      . "</csapi_reload_string_table>";
	$xmlData .= "<csapi_load_a_specific_configuration_file>"       . $actLoad_a_specific_configuration_file       . "</csapi_load_a_specific_configuration_file>";
	$xmlData .= "<csapi_the_specific_configuration_file>"          . $actThe_specific_configuration_file          . "</csapi_the_specific_configuration_file>";

	return(new ChangeSynergy::apiData(ChangeSynergy::util::callCsapi($aUser, $xmlData)));
}

sub packageInstall
{
	my $aUser		 = shift;
	my $packageName = shift;
	
	my $xmlData			= "";

	$xmlData .= "<csapi_action_flag>install_package</csapi_action_flag>";
	$xmlData .= "<csapi_token>"			. $aUser->getUserToken()	. "</csapi_token>";
	$xmlData .= "<csapi_role>"			. $aUser->getUserRole()		. "</csapi_role>";
	$xmlData .= "<csapi_database>"		. $aUser->getUserDatabase() . "</csapi_database>";
	$xmlData .= "<csapi_user>"			. $aUser->getUserName()		. "</csapi_user>";
	
	$xmlData .= "<csapi_package_name>"	. $packageName		        . "</csapi_package_name>";

	return(new ChangeSynergy::apiData(ChangeSynergy::util::callCsapi($aUser, $xmlData)));
}

sub getUserPreference
{
	my $aUser			= shift;
	my $actFlag			= shift;
	my $userName		= shift;
	my $preferenceName  = shift;
	
	my $xmlData			= "";

	$xmlData .= "<csapi_action_flag>"	 . $actFlag					 . "</csapi_action_flag>";
	$xmlData .= "<csapi_token>"			 . $aUser->getUserToken()	 . "</csapi_token>";
	$xmlData .= "<csapi_role>"			 . $aUser->getUserRole()	 . "</csapi_role>";
	$xmlData .= "<csapi_database>"		 . $aUser->getUserDatabase() . "</csapi_database>";
	$xmlData .= "<csapi_user>"			 . $aUser->getUserName()	 . "</csapi_user>";
	$xmlData .= "<csapi_username>"       . $userName                 . "</csapi_username>";
	$xmlData .= "<csapi_preferenceName>" . $preferenceName           . "</csapi_preferenceName>";

	return(new ChangeSynergy::apiData(ChangeSynergy::util::callCsapi($aUser, $xmlData)));
}

sub modifyUserPreferences
{
	my $aUser			= shift;
	my $userName		= shift;
	my $database		= shift;
	my $actionItem		= shift;
	my $keyName			= shift;
	my $keyValue		= shift;
	my $actionType      = shift;
	my $substitution    = shift;
	
	if(!defined($database))
	{
		$database = $aUser->getUserDatabase();	
	}
	elsif(($database eq "TRUE") || ($database eq "true"))
	{
		$database = "";
	}
	else
	{
		$database = $aUser->getUserDatabase();	
	}
		
	my $xmlData			= "";
	
	$xmlData .= "<csapi_action_flag>modify_user_preferences</csapi_action_flag>";
	$xmlData .= "<csapi_token>"			 . $aUser->getUserToken()	 . "</csapi_token>";
	$xmlData .= "<csapi_role>"			 . $aUser->getUserRole()	 . "</csapi_role>";
	$xmlData .= "<csapi_database>"		 . $aUser->getUserDatabase() . "</csapi_database>";
	$xmlData .= "<csapi_user>"			 . $aUser->getUserName()	 . "</csapi_user>";
	
	$xmlData .= "<csapi_username>"       . $userName   . "</csapi_username>";
	$xmlData .= "<csapi_database_name>"  . $database   . "</csapi_database_name>";
	$xmlData .= "<csapi_keyname>"        . $keyName    . "</csapi_keyname>";
	$xmlData .= "<csapi_action_item>"    . $actionItem . "</csapi_action_item>";
	$xmlData .= "<csapi_keyvalue>"       . $keyValue   . "</csapi_keyvalue>";
	$xmlData .= "<csapi_actiontype>"     . $actionType . "</csapi_actiontype>";
	$xmlData .= "<csapi_substitution>"   . $substitution . "</csapi_substitution>";

	return(new ChangeSynergy::apiData(ChangeSynergy::util::callCsapi($aUser, $xmlData)));
}

sub importUsers
{
	my $aUser			= shift;
	my $importSource    = shift;
	my $overwrite		= shift;
	my $importURL       = shift;
	my $importFile      = shift;
	my $importDelimiter = shift;
	my $importPassword  = shift;
	my $importEmail     = shift;
	my $importFirstname = shift;
	my $importLastname  = shift;

	my $xmlData			= "";
	
	$xmlData .= "<csapi_action_flag>import_users</csapi_action_flag>";
	$xmlData .= "<csapi_token>"			 . $aUser->getUserToken()	 . "</csapi_token>";
	$xmlData .= "<csapi_role>"			 . $aUser->getUserRole()	 . "</csapi_role>";
	$xmlData .= "<csapi_database>"		 . $aUser->getUserDatabase() . "</csapi_database>";
	$xmlData .= "<csapi_user>"			 . $aUser->getUserName()	 . "</csapi_user>";
	
	$xmlData .= "<csapi_import_source>"    . $importSource             . "</csapi_import_source>";
	$xmlData .= "<csapi_import_append>"    . $overwrite                . "</csapi_import_append>";
	$xmlData .= "<csapi_import_url>"       . $importURL                . "</csapi_import_url>";
	$xmlData .= "<csapi_import_file>"      . $importFile               . "</csapi_import_file>";
	$xmlData .= "<csapi_import_delimiter>" . $importDelimiter          . "</csapi_import_delimiter>";
	$xmlData .= "<csapi_import_password>"  . $importPassword           . "</csapi_import_password>";
	$xmlData .= "<csapi_import_email>"     . $importEmail              . "</csapi_import_email>";
	$xmlData .= "<csapi_import_firstname>" . $importFirstname          . "</csapi_import_firstname>";	
	$xmlData .= "<csapi_import_lastname>"  . $importLastname           . "</csapi_import_lastname>";	
	
	return(new ChangeSynergy::apiData(ChangeSynergy::util::callCsapi($aUser, $xmlData)));
}

sub callCsapi
{
	my $aUser	= shift;
	my $xmlData	= shift;
	my $ret_val	= "";
	my $soap	= "";

	#Add Soap envelope to XML data
	$soap  = "XML_CONTENT=<SOAP-ENV:Envelope>";
	$soap .=	"<SOAP-ENV:Body>";
	$soap .=		"<SOAP-ENV:Request>";
	$soap .=			escape($xmlData);
	$soap .=		"</SOAP-ENV:Request>";
	$soap .=	"</SOAP-ENV:Body>";
	$soap .= "</SOAP-ENV:Envelope>";

	#Setup connection through http to CsApi servelt
	#Create a user agent object
	my $ua = new LWP::UserAgent;
	$ua->agent("AgentName/0.1" . $ua->agent);
	$ua->timeout(600); 

	#Create a request
	my $URL = $protocol . '://' . $host . ':' . $port . '/servlet/CsAPI';

	my $req = new HTTP::Request("POST", $URL);

	#Pass XML data to CsAPI servlet
	$req->content_type('application/x-www-form-urlencoded');
	$req->content($soap);

	#Pass request to the user agent and get a response back
	my $res = $ua->request($req);

	#Check the outcome of the response
	if($res->is_success)
	{
		#Successful connection to server, check server return value
		my $faultcode	= 0;
		my $faultstring = "";

		#Get the fault code
		if($res->content =~ /<faultcode>(.*?)<\/faultcode>/gs)
		{
			$faultcode = $1;
		}

		if($res->content =~ /<faultstring>(.*?)<\/faultstring>/gs)
		{
			$faultstring = $1;
		}

		if($faultcode == 0)
		{
			#Get response data only
			if($res->content =~ /<csapi_response>(.*?)<\/csapi_response>/gs)
			{
				$ret_val = $1;
			}
			else
			{
				die "No response data found\n";
			}
		}
		else
		{
			#Get the fault string
			die "The fault code: $faultcode\nThe fault string: $faultstring\n";
		}
		return $ret_val;
	}
	else
	{
		#Connection failure
		die "Connection failure: The response as a string is: " . $res->as_string;
	}
}

sub callGetObject
{
	my $aUser	= shift;
	my $xmlData	= shift;
	my $fName	= shift;
	my $buffer	= shift;
	my $ret_val	= "";
	my $soap	= "";

	#Add Soap envelope to XML data
	$soap  = "XML_CONTENT=<SOAP-ENV:Envelope>";
	$soap .=	"<SOAP-ENV:Body>";
	$soap .=		"<SOAP-ENV:Request>";
	$soap .=			escape($xmlData);
	$soap .=		"</SOAP-ENV:Request>";
	$soap .=	"</SOAP-ENV:Body>";
	$soap .= "</SOAP-ENV:Envelope>";

	#Setup connection through http to CsApi servelt
	#Create a user agent object
	my $ua = new LWP::UserAgent;
	$ua->agent("AgentName/0.1" . $ua->agent);

	#Create a request
	my $URL = $protocol . '://' . $host . ':' . $port . '/servlet/CsAPI';

	my $req = new HTTP::Request("POST", $URL);

	#Pass XML data to CsAPI servlet
	$req->content_type('application/x-www-form-urlencoded');
	$req->content($soap);

	#Pass request to the user agent and get a response back
	my $res = $ua->request($req);

	#Check the outcome of the response
	if($res->is_success)
	{
		$buffer = $res->content;	
	}
	else
	{
		#Connection failure
		die "Connection failure: The response as a string is: " . $res->as_string;
	}

	return ($buffer);
}

sub callSetObjectOnServer
{
	my $aUser	= shift;
	my $buffer	= shift;
	my $size	= shift;
	my $ret_val	= "";
	
	#Setup connection through http to CsApi servelt

	#Create a user agent object
	my $ua = new LWP::UserAgent;
	$ua->agent("AgentName/0.1" . $ua->agent);

	#Create a request
	my $URL = $protocol . '://' . $host . ':' . $port . '/servlet/com.continuus.websynergy.servlet.CsOBJ?';

	my $req = new HTTP::Request("POST", $URL);

	#Pass XML data to CsAPI servlet
	$req->content_type('application/x-www-form-urlencoded');
	$req->content($buffer);

	#Pass request to the user agent and get a response back
	my $res = $ua->request($req);

	#Check the outcome of the response
	if($res->is_success)
	{
		#Successful connection to server, check server return value
		my $faultcode	= 0;
		my $faultstring = "";

		#Get the fault code
		if($res->content =~ /<faultcode>(.*?)<\/faultcode>/gs)
		{
			$faultcode = $1;
		}

		if($res->content =~ /<faultstring>(.*?)<\/faultstring>/gs)
		{
			$faultstring = $1;
		}

		if($faultcode == 0)
		{
			#Get response data only
			if($res->content =~ /<csapi_response>(.*?)<\/csapi_response>/gs)
			{
				$ret_val = $1;
			}
			else
			{
				die "No response data found\n";
			}
		}
		else
		{
			#Get the fault string
			die "The fault code: $faultcode\nThe fault string: $faultstring\n";
		}

		return $ret_val;
	}
	else
	{
		#Connection failure
		die "Connection failure: The response as a string is: " . $res->as_string;
	}
}

sub local_ServerSendFileBase
{
	my $aUser	= shift;
	my $buffer	= shift;
	my $size	= shift;
	
	if(!defined($aUser))
	{
		die "User information object is undef";
	}

	return(new ChangeSynergy::apiData(ChangeSynergy::util::callSetObjectOnServer($aUser, $buffer, $size)));
}

sub ServerSendFileBase
{
	my $aUser	= shift;
	my $buffer	= shift;
	my $size	= shift;

	if(!defined($aUser))
	{
		die "User information object is undef";
	}

	return(new ChangeSynergy::apiData(ChangeSynergy::util::callSetObjectOnServer($aUser, $buffer, $size)));
}

sub ServerGetFileBase
{
	my $aUser	= shift;
	my $file	= shift;
	my $xmlData = "";

	if(!defined($aUser))
	{
		die "User information object is undef";
	}

	$xmlData .= "<csapi_action_flag>get_server_file</csapi_action_flag>";
	$xmlData .= "<csapi_token>"			. $aUser->getUserToken()	. "</csapi_token>";
	$xmlData .= "<csapi_role>"			. $aUser->getUserRole()		. "</csapi_role>";
	$xmlData .= "<csapi_database>"		. $aUser->getUserDatabase() . "</csapi_database>";
	$xmlData .= "<csapi_user>"			. $aUser->getUserName()		. "</csapi_user>";
	$xmlData .= "<csapi_action_item>"	. $file						. "</csapi_action_item>";

	my $bData = undef;

	$bData = ChangeSynergy::util::callGetObject($aUser, $xmlData, $file);

	return(new ChangeSynergy::apiData($bData, undef));
}

sub CreateAttachmentObjectBase
{
	my $aUser			= shift;
	my $problemNumber	= shift;
	my $relation		= shift;
	my $attachmentName	= shift;
	my $webType			= shift;
	my $comment			= shift;
	my $type			= shift;
	my $isBinary		= shift;
	my $buffer			= shift;
	my $attachmentSize	= shift;

	if(!defined($aUser))
	{
		die "User information object is undef";
	}

	my $tmpFileName;

	my $tmp			= local_ServerSendFileBase($aUser, $buffer);
	$tmpFileName	= $tmp->getResponseData();
	my $xmlData		= "";

	$xmlData .= "<csapi_action_flag>create_cr_object</csapi_action_flag>";
	$xmlData .= "<csapi_token>"		. $aUser->getUserToken()	. "</csapi_token>";
	$xmlData .= "<csapi_role>"		. $aUser->getUserRole()		. "</csapi_role>";
	$xmlData .= "<csapi_database>"	. $aUser->getUserDatabase() . "</csapi_database>";
	$xmlData .= "<csapi_user>"		. $aUser->getUserName()		. "</csapi_user>";

	$xmlData .= "<csapi_cr_id>"				. $problemNumber		. "</csapi_cr_id>";
	$xmlData .= "<csapi_relation_name>"		. $relation				. "</csapi_relation_name>";
	$xmlData .= "<csapi_attachment_name>"	. $attachmentName		. "</csapi_attachment_name>";
	$xmlData .= "<csapi_attachment_size>"	. $attachmentSize		. "</csapi_attachment_size>";
	$xmlData .= "<csapi_web_type>"			. $webType				. "</csapi_web_type>";
	$xmlData .= "<csapi_type>"				. $type					. "</csapi_type>";
	$xmlData .= "<csapi_comment>"			. $comment				. "</csapi_comment>";
	$xmlData .= "<csapi_is_binary>"			. $isBinary				. "</csapi_is_binary>";
	$xmlData .= "<csapi_action_item>"		. $tmpFileName			. "</csapi_action_item>";

	return(new ChangeSynergy::apiData(ChangeSynergy::util::callCsapi($aUser, $xmlData)));
}

sub DatabaseSetObjectBase
{
	my $aUser		= shift;	
	my $cvid		= shift;
	my $comment		= shift;
	my $buffer		= shift;
	my $size		= shift;

	if(!defined($aUser))
	{
		die "User information object is undef";
	}

	my $tmpFileName;
	my $tmp			= local_ServerSendFileBase($aUser, $buffer, $size);
	$tmpFileName	= $tmp->getResponseData();
	my $xmlData		= "";

	$xmlData .= "<csapi_action_flag>set_object</csapi_action_flag>";
	$xmlData .= "<csapi_token>"		. $aUser->getUserToken()	. "</csapi_token>";
	$xmlData .= "<csapi_role>"		. $aUser->getUserRole()		. "</csapi_role>";
	$xmlData .= "<csapi_database>"	. $aUser->getUserDatabase() . "</csapi_database>";
	$xmlData .= "<csapi_user>"		. $aUser->getUserName()		. "</csapi_user>";

	$xmlData .= "<csapi_cvid>"				. $cvid				. "</csapi_cvid>";
	$xmlData .= "<csapi_action_item>"		. $tmpFileName		. "</csapi_action_item>";
	$xmlData .= "<csapi_attachment_size>"	. $size				. "</csapi_attachment_size>";
	$xmlData .= "<csapi_comment>"			. $comment			. "</csapi_comment>";

	return(new ChangeSynergy::apiData(ChangeSynergy::util::callCsapi($aUser, $xmlData)));
}

sub DatabaseGetObjectBase
{
	my $aUser		= shift;
	my $cvid		= shift;
	my $xmlData		= "";

	if(!defined($aUser))
	{
		die "User information object is undef";
	}

	$xmlData .= "<csapi_action_flag>get_object</csapi_action_flag>";
	$xmlData .= "<csapi_token>"		. $aUser->getUserToken()	. "</csapi_token>";
	$xmlData .= "<csapi_role>"		. $aUser->getUserRole()		. "</csapi_role>";
	$xmlData .= "<csapi_database>"	. $aUser->getUserDatabase() . "</csapi_database>";
	$xmlData .= "<csapi_user>"		. $aUser->getUserName()		. "</csapi_user>";
	$xmlData .= "<csapi_cvid>"		. $cvid						. "</csapi_cvid>";

	my $bData = undef;

	$bData = ChangeSynergy::util::callGetObject($aUser, $xmlData, $cvid);

	return(new ChangeSynergy::apiData($bData, undef));
}

sub ModifyObjectsAction
{
	my $aUser     = shift;
	my $cvidList  = shift;
	my $attrData  = shift;
	my $iType     = shift;
	
	if(!defined($aUser))
	{
		die "User information object is undef";
	}

	if(!defined($attrData))
	{
		die "Data information object is undef";
	}

	my $xmlData   = "";
	my $xmlAction = "";
	my $tmp       = $attrData->toObjectXml($iType);
	my $globals   = new ChangeSynergy::Globals();

	if($iType == $globals->{CSAPI_CV_ATTR_CREATE})
	{
		$xmlAction = "create_cv_attr";
	}
	elsif($iType == $globals->{CSAPI_CV_ATTR_MODIFY})
	{
		$xmlAction = "modify_cv_attr";
	}
	elsif($iType == $globals->{CSAPI_CV_ATTR_DELETE})
	{
		$xmlAction = "delete_cv_attr";
	}

	$xmlData .= "<csapi_action_flag>" . $xmlAction                . "</csapi_action_flag>";
	$xmlData .= "<csapi_token>"		  . $aUser->getUserToken()	  . "</csapi_token>";
	$xmlData .= "<csapi_role>"		  . $aUser->getUserRole()     . "</csapi_role>";
	$xmlData .= "<csapi_database>"	  . $aUser->getUserDatabase() . "</csapi_database>";
	$xmlData .= "<csapi_user>"		  . $aUser->getUserName()	  . "</csapi_user>";

	$xmlData .= "<csapi_cv_owners>"   . $cvidList                 . "</csapi_cv_owners>";
	$xmlData .= $tmp;

	return(new ChangeSynergy::apiData(ChangeSynergy::util::callCsapi($aUser, $xmlData)));
}

sub NewCVOperation
{
	my $aUser   = shift;
	my $subsys  = shift;
	my $cvtype  = shift;
	my $name    = shift;
	my $version = shift; 
	my $state   = shift;
	my $bCreate = shift;
	my $xmlData = "";

	if(!defined($aUser))
	{
		die "User information object is undef";
	}

	if($bCreate eq "TRUE")
	{
		$xmlData .= "<csapi_action_flag>create_new_cv</csapi_action_flag>";
	}
	else
	{
		$xmlData .= "<csapi_action_flag>delete_new_cv</csapi_action_flag>";
	}

	$xmlData .= "<csapi_token>"		  . $aUser->getUserToken()	  . "</csapi_token>";
	$xmlData .= "<csapi_role>"		  . $aUser->getUserRole()     . "</csapi_role>";
	$xmlData .= "<csapi_password>"    . $aUser->getUserPassword() . "</csapi_password>";
	$xmlData .= "<csapi_database>"	  . $aUser->getUserDatabase() . "</csapi_database>";
	$xmlData .= "<csapi_user>"		  . $aUser->getUserName()	  . "</csapi_user>";

	$xmlData .= "<csapi_cv_subsys>"   . $subsys                   . "</csapi_cv_subsys>";
	$xmlData .= "<csapi_cv_type>"     . $cvtype                   . "</csapi_cv_type>";
	$xmlData .= "<csapi_cv_name>"     . $name                     . "</csapi_cv_name>";
	$xmlData .= "<csapi_cv_version>"  . $version                  . "</csapi_cv_version>";

	if($bCreate eq "TRUE")
	{
		$xmlData .= "<csapi_cv_state>" . $state . "</csapi_cv_state>";
	}

	return(new ChangeSynergy::apiData(ChangeSynergy::util::callCsapi($aUser, $xmlData)));
}

sub RefreshUsers
{
	my $aUser   = shift;

	die "User information object is undef" if !defined($aUser);

	my $xmlData = "<csapi_token>" . $aUser->getUserToken() . "</csapi_token>";
	
	$xmlData .= "<csapi_role>"		  . $aUser->getUserRole()     . "</csapi_role>";
	$xmlData .= "<csapi_password>"    . $aUser->getUserPassword() . "</csapi_password>";
	$xmlData .= "<csapi_database>"	  . $aUser->getUserDatabase() . "</csapi_database>";
	$xmlData .= "<csapi_user>"		  . $aUser->getUserName()	  . "</csapi_user>";

	$xmlData .= "<csapi_action_flag>refresh_cm_security_and_users</csapi_action_flag>";

	return new ChangeSynergy::apiData(ChangeSynergy::util::callCsapi($aUser, $xmlData));
}

sub escape
{
	my $buffer  = shift;

	if(!defined($buffer))
	{
		return "";
	}

	return (CGI::Util::escape($buffer));
}

sub unescape
{
	my $buffer  = shift;

	if(!defined($buffer))
	{
		return "";
	}

	return (CGI::Util::unescape($buffer));
}

sub htmlEncode
{
	my $buffer = shift;

	if(!defined($buffer))
	{
		return "";
	}

	$buffer =~ s/&/&amp;/g;
	$buffer =~ s/</&lt;/g;
	$buffer =~ s/>/&gt;/g;
	$buffer =~ s/\r\n/<BR>/g;
	$buffer =~ s/\n/<BR>/g;
	$buffer =~ s/\t/&nbsp;&nbsp;&nbsp;&nbsp;/g;
	$buffer =~ s/  /&nbsp;&nbsp;/g;
	$buffer =~ s/"/&quot;/g;
	$buffer =~ s/'/&#039;/g;
	$buffer =~ s/NULL/&nbsp;/g;

	return $buffer;
}

sub xmlEncode
{
	my $buffer  = shift;

	if(!defined($buffer))
	{
		return "";
	}

	$buffer =~ s/&/&amp;/g;
	$buffer =~ s/</&lt;/g;
	$buffer =~ s/>/&gt;/g;

	return ($buffer);
}

sub xmlDecode
{
	my $buffer  = shift;

	if(!defined($buffer))
	{
		return "";
	}
	
	$buffer =~ s/&lt;/</g;
	$buffer =~ s/&gt;/>/g;
	$buffer =~ s/&amp;/&/g;

	return $buffer;
}

1;

__END__
